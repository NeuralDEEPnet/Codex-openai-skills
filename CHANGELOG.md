# Changelog

## v0.3.1 — Print path inspected — 2026-11-08

- **3DJ capability reference** (`create-model/references/capabilities.md`): catalogue re-observed on 2026-11-08. `cad_validate_script` now builds and measures in the isolated kernel (with an optional PNG preview); `cad_render_views`, `cad_check_assembly`, `cad_export_model` (STL/STEP/GLB/ZIP with a download URL), `cad_save_model`, `cad_import_model`, `compose_design_brief` and `openscad_compile_model` are advertised live. The 2026-10-11 baseline is kept as history. Account tools were not executed; discovery at run time still decides.
- **create-model**: the Replicad path now runs validate → render → assembly check → export/save, with the "no file until the export URL returns" rule kept; explicit no-connector fallback.
- **interactive-3d-print-design, parametric-printable-surfaces, print-production**: descriptions now say when to trigger and when not to; each links to the shared process (`3d-object-design` → design-core) so depth, lean delivery and the reduction pass apply; explicit relative paths replace "the companion 3DJ skill"; a parameter-map table and a handoff shape added; no-connector fallbacks stated.
- **3d-object-design** and `docs/NEURALDEEP-INTEGRATIONS.md`: the optional 3dj.app mention names the view, assembly and export tools for the "review the actual model" step.
- **Validator** (`scripts/build_plugin.py`): explicit checks with messages instead of bare asserts; checks description length, relative references inside skills, every eval case (case.yaml name, prompt, grader frontmatter), task and trigger-query skill names, a trigger query for every skill, and a changelog entry for the manifest version.
- **Evals**: graded case `acoustic-tile-honesty` (6 checks), tasks print-01…04, 8 trigger queries for the four print skills. Structural checks pass; no behavioral run yet.
- **Inspection** (no change needed): every contrast ratio claimed in `house-style.md` recomputed with the WCAG 2.x formula and found correct to one decimal; every relative reference in the skills resolves; all descriptions are under 1,024 characters.

## v0.3 — Lean and clean — 2026-11-05

- **House style** (`design-core/references/house-style.md`): Neuraldeep's lean and clean philosophy in two layers. *Lean delivery* always: answer first, artifacts not essays, one next step, response budgets per depth (Rapid ≤ 400 words, Standard ≤ 1,200 plus tables), subtract before you add, targeted revisions stay targeted. *Clean default character* only when a brief has no brand of its own: one ink, one paper, one accent; whitespace as structure; two type weights; one-line copy; honest surfaces; anti-principles and starter tokens (light and dark, AA contrast computed) derived from neuraldeep.net. Evidence, owner intent and inference are tagged separately; branded work stays style-agnostic.
- **Reduction pass** in every specialist skill and in the director's cross-medium critique.
- **software-design**: lean system defaults, a copy section, dark-theme render check. **design-core**: targeted-revision rule, depth budgets, learning capture pointer kept. **3d-object-design**: production evidence retained; reduction pass added.
- **Evals**: graded case `lean-unbranded-landing` (9 checks), tasks lean-01…04, 6 trigger queries. Not yet run against a model.
- Skill bodies are shared with the Claude edition (`NeuralDEEPnet/claude-design-skills` v0.4.0); the 3D skill keeps the 3dj.app connector wording here.

## v0.2 — 2026-10-28

- **Depth modes** in design-core (Rapid / Standard / Full) so quick asks don't get a 13-stage document, while DNA and real-output review always survive.
- **Templates** for brief, research log, inspiration panel, user panel, DNA, concept card, senior review, synthesis, handoff (`design-core/references/templates.md`).
- **Specialists load design-core explicitly** (relative path) with a compact fallback sequence, so Codex doesn't skip the shared process.
- **Concrete checks**: WCAG 2.2 AA numbers and Core Web Vitals (software), flash/caption rules and UI duration tiers (motion), FDM/SLA/moulding rules (3D), comfort and frame-time budgets (virtual worlds), crop/size checks and identity-mark rules (image).
- **Evidence tags** `[evidence] [opinion] [trend] [inspiration] [inference]` and a "design implications" close for research.
- **Director** routing table (incl. logo/identity and packaging), dependency sequencing, handoff block, cross-medium critique.
- **Optional Neuraldeep integrations** named at the right production steps (SketchMonkey for images/video, 3dj.app for CAD/print/blockouts), each with generic alternatives.
- **Descriptions** rewritten with natural trigger phrases and clearer exclusions.
- **Evals**: 3 graded cases, 3 new tasks, 14 trigger queries; results in `docs/EVAL-RESULTS.md`.

## v0.1

- Studio foundation: design-director, design-core and five specialist skills.
