"""Validate the repository and build the portable plugin from the canonical skills.

Checks structure only: skill frontmatter, relative references, eval layout and the
package contents. It says nothing about design performance; run the evals for that.
"""
from pathlib import Path
import json
import re
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / ".agents/skills"
EVALS = ROOT / "evals"
NAME_RE = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
# Backticked relative paths inside a skill, e.g. `../design-core/SKILL.md`, `references/templates.md`.
REF_RE = re.compile(r"`((?:\.\./|references/|assets/)[^`<>]+)`")
MAX_NAME = 64
MAX_DESCRIPTION = 1024

errors: list[str] = []


def check(condition: bool, message: str) -> None:
    if not condition:
        errors.append(message)


def frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    check(text.startswith("---\n"), f"{path}: missing YAML frontmatter")
    header = text.split("---", 2)[1] if text.startswith("---\n") else ""
    fields: dict[str, str] = {}
    for line in header.splitlines():
        if ":" in line and not line.startswith((" ", "\t")):
            key, _, value = line.partition(":")
            fields[key.strip()] = value.strip()
    return fields


def validate_skills() -> list[tuple[Path, str]]:
    files: list[tuple[Path, str]] = []
    for folder in sorted(p for p in SKILLS.iterdir() if p.is_dir()):
        skill = folder / "SKILL.md"
        check(skill.is_file(), f"{folder.name}: SKILL.md missing")
        if not skill.is_file():
            continue
        check(NAME_RE.fullmatch(folder.name) is not None and len(folder.name) <= MAX_NAME,
              f"{folder.name}: directory must be kebab-case and at most {MAX_NAME} characters")
        fields = frontmatter(skill)
        check(fields.get("name") == folder.name, f"{folder.name}: frontmatter name must equal the directory name")
        description = fields.get("description", "")
        check(0 < len(description) <= MAX_DESCRIPTION,
              f"{folder.name}: description must be 1–{MAX_DESCRIPTION} characters (is {len(description)})")
        check("TODO" not in skill.read_text(encoding="utf-8"), f"{folder.name}: SKILL.md contains TODO")
        for path in sorted(folder.rglob("*")):
            check(not path.is_symlink(), f"symlink not allowed: {path}")
            if path.is_file():
                files.append((path, "skills/" + path.relative_to(SKILLS).as_posix()))
                if path.suffix == ".md":
                    for ref in REF_RE.findall(path.read_text(encoding="utf-8")):
                        target = (path.parent / ref).resolve()
                        check(target.exists(), f"{path.relative_to(ROOT)}: reference `{ref}` does not exist")
    return files


def validate_evals() -> int:
    tasks = [json.loads(line) for line in (EVALS / "tasks.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
    ids = [t.get("id") for t in tasks]
    check(len(set(ids)) == len(ids), "evals/tasks.jsonl: duplicate task ids")
    for task in tasks:
        check(isinstance(task.get("prompt"), str) and task["prompt"].strip(), f"task {task.get('id')}: prompt missing")
        check((SKILLS / str(task.get("skill")) / "SKILL.md").is_file(), f"task {task.get('id')}: unknown skill {task.get('skill')}")
        acceptance = task.get("acceptance", [])
        check(isinstance(acceptance, list) and all(isinstance(a, str) for a in acceptance),
              f"task {task.get('id')}: acceptance must be a list of strings")

    triggers = json.loads((EVALS / "trigger-evals.json").read_text(encoding="utf-8"))
    check(isinstance(triggers, list) and triggers, "evals/trigger-evals.json: must be a non-empty list")
    for i, item in enumerate(triggers):
        check(isinstance(item.get("query"), str) and item["query"].strip(), f"trigger-evals[{i}]: query missing")
        check((SKILLS / str(item.get("skill")) / "SKILL.md").is_file(), f"trigger-evals[{i}]: unknown skill {item.get('skill')}")
        check(isinstance(item.get("should_trigger"), bool), f"trigger-evals[{i}]: should_trigger must be true or false")
    covered = {item["skill"] for item in triggers if isinstance(item, dict)}
    for folder in sorted(p for p in SKILLS.iterdir() if p.is_dir()):
        check(folder.name in covered, f"evals/trigger-evals.json: no trigger query for skill {folder.name}")

    cases = sorted(p for p in (EVALS / "cases").iterdir() if p.is_dir())
    for case in cases:
        meta = case / "case.yaml"
        check(meta.is_file(), f"{case.name}: case.yaml missing")
        if meta.is_file():
            check(f"name: {case.name}" in meta.read_text(encoding="utf-8"), f"{case.name}: case.yaml name must equal the directory name")
        prompt = case / "prompt.md"
        check(prompt.is_file(), f"{case.name}: prompt.md missing")
        if prompt.is_file():
            body = prompt.read_text(encoding="utf-8").split("---", 2)[-1].strip()
            check(bool(body), f"{case.name}: prompt.md has no prompt text")
        graders = sorted((case / "graders").glob("*.md")) if (case / "graders").is_dir() else []
        check(bool(graders), f"{case.name}: no graders")
        for grader in graders:
            fields = frontmatter(grader)
            check(fields.get("type") in {"llm", "code"}, f"{grader.relative_to(ROOT)}: type must be llm or code")
            statement = grader.read_text(encoding="utf-8").split("---", 2)[-1].strip()
            check(bool(statement), f"{grader.relative_to(ROOT)}: empty assertion")
    return len(tasks) + len(triggers) + len(cases)


def build() -> Path:
    manifest = json.loads((ROOT / "plugin.json").read_text(encoding="utf-8"))
    name = manifest["name"]
    check(NAME_RE.fullmatch(name) is not None and len(name) <= MAX_NAME, "plugin.json: invalid name")
    check(re.fullmatch(r"\d+\.\d+\.\d+", manifest["version"]) is not None, "plugin.json: version must be semver")
    check(len(manifest["extensions"]["com.openai"]["interface"]["shortDescription"]) <= 30,
          "plugin.json: shortDescription over 30 characters")
    changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    check(f"v{manifest['version']}" in changelog, f"CHANGELOG.md has no entry for v{manifest['version']}")

    files = [(ROOT / "plugin.json", "plugin.json"), (ROOT / "LICENSE", "LICENSE")] + validate_skills()
    eval_count = validate_evals()

    if errors:
        print("Validation failed:")
        for message in errors:
            print(f"  - {message}")
        sys.exit(1)

    out = ROOT / "dist" / f"{name}-{manifest['version']}.zip"
    out.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as archive:
        for path, relative in files:
            info = zipfile.ZipInfo(f"{name}/{relative}", (2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, path.read_bytes())
    with zipfile.ZipFile(out) as archive:
        check(archive.testzip() is None, "built archive failed its integrity test")
        check(len(archive.namelist()) == len(files), "built archive is missing files")
    if errors:
        print("\n".join(errors))
        sys.exit(1)
    skill_count = len(list(SKILLS.glob("*/SKILL.md")))
    print(f"Validated {skill_count} skills and {eval_count} eval items (tasks, trigger queries, graded cases); built {out}")
    return out


if __name__ == "__main__":
    build()
