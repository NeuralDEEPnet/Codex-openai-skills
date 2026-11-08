---
name: create-model
description: Create, measure, render, export or retrieve 3D models through the Neuraldeep 3DJ connector — text- or image-to-mesh for decorative geometry, OpenSCAD compile-and-measure, and parametric Replicad/OpenCascade CAD with STL, STEP and GLB export, assembly checks and gallery saves. Use when a 3DJ connector is available and the user wants a model built, checked, exported or fetched ("make a printable bracket and give me the STEP", "render this part from the front", "show my saved models"). Do not use for the design process itself (3d-object-design), and when no connector is available fall back to portable OpenSCAD or CAD source and say it was not compiled.
---

# 3DJ model studio

Use the connected 3DJ MCP tools. Discover the actual catalogue before calling tools; the names observed so far are recorded in `references/capabilities.md`. Never invent modelling, export, checkout, or shipping tools. The design thinking (package, DNA, architectures, reduction pass) comes from `../3d-object-design/SKILL.md`; this skill is the production path.

1. Establish the object, intended use, overall dimensions in millimetres, and any required interfaces. Ask only for dimensions that affect function; otherwise state provisional dimensions and proceed. Distinguish decorative mesh generation from measured parametric CAD.
2. **Decorative geometry.** Call `list_providers`, then `generate_from_text` or `generate_from_image_url`. Image input must be a direct public HTTPS image URL; do not publish private attachments to make a URL. Generation consumes the user's allowance. Return the modelId, poll with `get_generation_status`, and pass through actual failures. A successful start is not a finished model.
3. **Measured OpenSCAD meshes.** Prefer `openscad_get_starters` (public) and `openscad_compile_model` (account; compiles in the real isolated engine and returns effective source, parameters, triangle count, closed-mesh measurements and optional axis-aligned build-volume fit — pass the printer volume when known, e.g. Prusa MINI `[180,180,180]`). Compilation uses a validation allowance, not generation credits. It does not save a gallery record or return an STL download; export the STL in the 3DJ OpenSCAD workbench or with a local OpenSCAD. Axis-aligned fit excludes supports and brims; measurements do not certify mechanical fit or manufacturing safety.
4. **Measured solid CAD (Replicad/OpenCascade DSL).** Start from `cad_get_starters`, adapt the script and its `Param.*` declarations, then work in this order, calling only what live discovery exposes:
   - `cad_validate_script` builds the script in the isolated kernel and returns bounds, volume, per-body closed-mesh checks, DfAM checks and bed fit; `preview: true` returns an isometric PNG. No file is written.
   - `cad_render_views` returns orthographic and isometric PNGs (thin-wall and overhang highlights, section planes) — use it to look at the real part, not just its numbers.
   - `cad_check_assembly` for multi-part scripts: interference volumes, minimum clearance, joint sweeps.
   - `cad_import_model` to design around an existing STEP/STL/GLB (enclosure around a PCB, bracket to a fitting).
   - `cad_export_model` writes the downloadable file (`stl`, `stl-fins`, `step`, `glb`, `zip` with BOM) and returns a download URL with measurements; `cad_save_model` saves an editable gallery model with revision history and an STL. Both use the account's allowance.
   - `compose_design_brief` turns a built script into a product-render brief with a reference image for SketchMonkey or any renderer.
   Every measurement is a geometry diagnostic, not a structural or safety certification. Do not say a STEP/STL file exists until the export call returned its URL.
5. Use `list_my_models`, `cad_list_models`, and `get_model_download_url` only for the authenticated user's models. Report the format actually returned. A GLB download is not automatically an STL or a print-ready part. Do not claim that supportedExports proves a corresponding file is available.
6. Present the result with dimensions, assumptions, the views you inspected, the downloadable assets actually returned, and the next edit that would improve function. When fabrication is requested, use `../print-production/SKILL.md`.

**Without the connector:** write portable `.scad` or Replicad source with the same parameters, state in one line that it has not been compiled or exported here, and give the user the compile and export steps (3DJ workbench, OpenSCAD, FreeCAD, or a `trimesh` check on the exported bytes).

Authentication: public CAD starters, validation, renders, assembly checks and design briefs work without an account key. Account tools require a user-owned Bearer API key minted at https://3dj-neuraldeepnet.on.adaptive.ai/agents. Use the host's supported secure credential settings. Never request a key in chat, save it in a plugin file, reuse the founder's key for customers, or describe API-key authentication as OAuth. If the host cannot provide the key, explain the connection limitation and continue public CAD work.

Brand: 3DJ · 3dj.app · Idea to production: in no time!
