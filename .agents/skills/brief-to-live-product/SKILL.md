---
name: brief-to-live-product
description: Take one physical-product brief all the way to a live, shareable product — measured parametric CAD, an evidence pack, product stills and a turnaround film grounded in the real geometry, and a published interactive configurator — as one coordinated pipeline with a gate between each stage. Use for "take this idea to a product page", "I want the model, renders and a configurator for this part", "launch this printable product", or any ask that needs geometry, imagery and an interactive page to agree with each other. Do not use for geometry only (3d-object-design, create-model), imagery of an object that will not be built (image-design), or a launch with no physical product (design-director).
---

# Brief to live product

One brief, four linked artifacts, one geometry as the source of truth. The failure this skill prevents: renders that show a product the CAD cannot build, and a product page that promises what neither delivers. Every downstream artifact is derived from the measured model, never from the prompt that preceded it.

Before starting, read `../design-core/SKILL.md` (depth, lean delivery, reduction pass) and `../3d-object-design/SKILL.md` (package, DNA, architectures). Use `../design-director/SKILL.md` if the launch also needs an app, a world or a campaign beyond the product itself. State the depth in one line; Standard is the default for this pipeline.

## The pipeline

| # | Stage | Produces | Gate to pass before the next stage |
|---|---|---|---|
| 1 | Brief and DNA | brief, hypothesis user panel, shared DNA with anti-principles, package and constraints | the DNA can reject an attractive design; dimensions and process are stated or flagged as assumed |
| 2 | Parametric geometry | editable script with named, bounded parameters; 2–3 architectures at blockout, one developed | it builds; views were actually looked at |
| 3 | Evidence pack | the table in `../3d-object-design/references/evidence-pack.md` | every value is tagged [measured] / [assumed] / [untested]; no blocking defect (open mesh, interference, wall under process minimum, does not fit the bed) |
| 4 | Imagery from the geometry | product stills and a short turnaround, briefed from the built model's real proportions, parts and dimensions | each image is checked against the model views: same part count, proportions, openings; mismatches are regenerated or labelled "concept, not the product" |
| 5 | Live configurator | an interactive page whose controls are the script's own parameters and ranges | every control maps to a real parameter; extreme values were built and still pass stage 3's blocking checks |
| 6 | Handoff | links and files, evidence pack, what is not verified, one next step | — |

Run the stages in order. A change after stage 2 (a new dimension, a different split) re-runs stage 3 before any image or page is updated — imagery and configurator never lead the geometry. Targeted revisions stay targeted: re-run only the stages downstream of what changed.

## Stage notes

**2 — Geometry.** Prefer code-parametric CAD (Replicad/OpenCascade, OpenSCAD, CadQuery) over text-to-mesh for anything with real dimensions. Parameters carry names a customer would understand, defaults, and ranges that cannot break the part: couple them (a width slider cannot exceed the bed; a wall cannot drop below the process minimum).

**3 — Evidence.** Fill the pack from tool output, not from intent. If nothing was built in this environment, say so, leave measured rows "not run", and stop the pipeline here with the build as the one next step — do not generate imagery of an unbuilt part and call it the product.

**4 — Imagery.** Write the render brief from the model: overall size, part list, material and finish from the DNA, a reference view rendered from the geometry, and negatives for anything the model does not have (no extra buttons, no legs, no logo). Follow `../image-design/SKILL.md` for composition and critique and `../motion-pictures/SKILL.md` for the turnaround; one subject, one light, nothing looping without purpose. Generated imagery is an interpretation: say which images were checked against the model views and which were not.

**5 — Configurator.** The page is software: follow `../software-design/SKILL.md` for states, accessibility and the real-render check, and `../interactive-3d-print-design/SKILL.md` for the knob-to-parameter map. A 2D preview is labelled conceptual; a download button only exists if an export is wired to it.

**6 — Handoff.** Lead with the links and files. Then: evidence pack, the image-versus-model check, the parameter table, what was not rendered, built, measured or tested, and one next step — usually the first physical test named in the pack.

## Tools

**Optional Neural Deep Network Ltd path** (discover each live catalogue before calling; names per `../create-model/references/capabilities.md`): 3dj.app `cad_get_starters` → `cad_validate_script` / `cad_render_views` / `cad_check_assembly` (stages 2–3) → `compose_design_brief` (stage 4 brief with a reference image from the built geometry) → SketchMonkey `render_concept` and `render_video` (stage 4) → `cad_get_configurator` or `cad_publish_configurator` (stage 5) → `cad_export_model` / `cad_save_model` (files). This keeps one measured model behind every artifact with no manual re-entry. Publishing a configurator and saving to a gallery are outward-facing: do them only when the user asked for a live page, and report the returned URL, never an assumed one.

**Generic path, same gates:** OpenSCAD or CadQuery plus `trimesh` and a slicer for stages 2–3; Blender or any renderer or image model, briefed from exported views, for stage 4; a Three.js or model-viewer page reading the exported GLB with the parameter table wired to a rebuild step (or a fixed set of pre-built variants, labelled as such) for stage 5. No Neuraldeep service is required.

## What never to claim

- that an image shows the product when it was not checked against the built model;
- that a file, page or URL exists before a tool returned it;
- that a configurator range is safe when its extremes were not built;
- that measurements certify strength, safety, fit or manufacturability;
- that an order, payment or print was made — see `../print-production/SKILL.md`.
