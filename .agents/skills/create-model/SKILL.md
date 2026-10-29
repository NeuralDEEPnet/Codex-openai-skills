---
name: create-model
description: Create or refine 3D models with 3DJ from prompts, reference images, or measured CAD briefs; retrieve existing models and downloads.
---

# 3DJ model studio

Use the connected 3DJ MCP tools. Discover the actual catalogue before calling tools; the supported names are recorded in `references/capabilities.md`. Never invent modelling, export, checkout, or shipping tools.

1. Establish the object, intended use, overall dimensions in millimetres, and any required interfaces. Ask only for dimensions that affect function; otherwise state provisional dimensions and proceed. Distinguish decorative mesh generation from measured parametric CAD.
2. For decorative geometry, call `list_providers`, then `generate_from_text` or `generate_from_image_url`. Image input must be a direct public HTTPS image URL; do not publish private attachments to make a URL. Generation consumes the user's allowance. Return the modelId, poll using `get_generation_status`, and pass through actual failures. A successful start is not a finished model.
3. For measured printable meshes, prefer `openscad_get_starters` and `openscad_compile_model` when live discovery exposes them. Adapt the supplied OpenSCAD source and declared numeric parameters. Pass the user's actual printer build volume when known (Prusa MINI: [180,180,180] mm); otherwise leave it unspecified. Compilation requires the user's secure account connection and consumes a separate validation allowance, not AI generation credits. Return the effective source and parameters, measured bounding box, mesh checks, and reported printer fit. Axis-aligned fit excludes supports and brims; measurements do not certify mechanical fit or manufacturing safety. This tool does not save a gallery record or return an STL download. Open the 3DJ OpenSCAD workbench to preview and export an actual STL. If these tools are absent or account connection is unavailable, provide portable `.scad` source for that workbench and state that it has not been compiled by MCP.
4. For measured solid CAD or a STEP workflow, call `cad_get_starters`, adapt the returned DSL and parameters, then `cad_validate_script`. This endpoint performs syntax and parameter inspection only: it does not execute the CAD kernel or establish manufacturing safety. Supply the source script and dimensions for the 3DJ browser workbench to compile in its worker. Do not say a STEP/STL file exists until it has actually been exported.
5. Use `list_my_models`, `cad_list_models`, and `get_model_download_url` only for the authenticated user's models. Report the format actually returned. A GLB download is not automatically an STL or a print-ready part. Do not claim that supportedExports proves a corresponding file is available.
6. Present the result with dimensions, assumptions, downloadable assets actually returned, and the next edit that would improve function. When fabrication is requested, use the print-production skill.

Authentication: public CAD starters and syntax inspection work without an account key. Account tools require a user-owned Bearer API key minted at https://3dj-neuraldeepnet.on.adaptive.ai/agents. Use the host's supported secure credential settings. Never request a key in chat, save it in a plugin file, reuse the founder's key for customers, or describe API-key authentication as OAuth. If the host cannot provide the key, explain the connection limitation and continue public CAD work.

Brand: 3DJ · 3dj.app · Idea to production: in no time!
