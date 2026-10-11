"""Build the portable plugin from canonical repository-local skills."""
from pathlib import Path
import json, re, zipfile
ROOT = Path(__file__).resolve().parents[1]
def build():
    manifest = json.loads((ROOT / "plugin.json").read_text())
    name = manifest["name"]
    assert re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) and len(name) <= 64
    assert re.fullmatch(r"\d+\.\d+\.\d+", manifest["version"])
    assert len(manifest["extensions"]["com.openai"]["interface"]["shortDescription"]) <= 30
    files = [(ROOT / "plugin.json", "plugin.json"), (ROOT / "LICENSE", "LICENSE")]
    skills = ROOT / ".agents/skills"
    for folder in sorted(skills.iterdir()):
        if not folder.is_dir(): continue
        text = (folder / "SKILL.md").read_text()
        assert text.startswith("---\n")
        header = text.split("---", 2)[1]
        assert f"name: {folder.name}\n" in header
        assert "description: " in header
        assert "TODO" not in text
        for path in sorted(folder.rglob("*")):
            assert not path.is_symlink(), f"Symlink: {path}"
            if path.is_file():
                files.append((path, "skills/" + path.relative_to(skills).as_posix()))
    tasks = [json.loads(line) for line in (ROOT / "evals/tasks.jsonl").read_text().splitlines() if line]
    assert len({t["id"] for t in tasks}) == len(tasks)
    assert all((skills / t["skill"] / "SKILL.md").is_file() for t in tasks)
    out = ROOT / "dist" / f"{name}-{manifest['version']}.zip"
    out.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as archive:
        for path, relative in files:
            info = zipfile.ZipInfo(f"{name}/{relative}", (2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, path.read_bytes())
    with zipfile.ZipFile(out) as archive:
        assert archive.testzip() is None
        assert len(archive.namelist()) == len(files)
    print(f"Validated {len(list(skills.glob('*/SKILL.md')))} skills and {len(tasks)} eval prompts; built {out}")
    return out
if __name__ == "__main__": build()
