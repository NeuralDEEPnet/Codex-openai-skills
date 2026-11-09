# Verified capabilities

Endpoint: https://3dj-neuraldeepnet.on.adaptive.ai/api/mcp · Transport: stateless Streamable HTTP, POST JSON-RPC.

Two observations are recorded here. Discovery at run time always wins: use a tool only when the live `tools/list` exposes it, and pass only fields its live schema accepts.

## Catalogue observed 2026-11-08

Source: the connector's advertised tool list and tool descriptions as seen from an agent session on that date. Descriptions were read; successful execution of account tools was **not** exercised in that session. "Account" means the description states a per-account allowance or owned data; "public" means the description states public, throttled access; "not checked" means the description did not say.

| Tool | Account | What it does (per its description) | What it does not do |
| --- | --- | --- | --- |
| cad_get_starters | public | Editable Replicad/OpenCascade starter scripts and DSL reference (`index: true` for a compact index) | — |
| cad_validate_script | public | Builds the script in the isolated kernel: syntax, `Param.*` declarations, bounds, volume, per-body closed-mesh checks, DfAM checks, bed fit; `preview: true` returns an isometric PNG | Writes no file; not a manufacturing certification |
| cad_render_views | public | Orthographic/isometric PNGs (`iso`, `front`, `top`, `right`) as image content; thin-wall and overhang highlights; section planes | — |
| cad_check_assembly | public | Pairwise interference volumes, minimum clearance, `placeAt` joint sweeps across `Param` ranges | — |
| compose_design_brief | public | Builds and measures a script, renders a reference PNG, composes a photoreal render brief with import steps for Blender, FreeCAD, Fusion 360, Onshape, slicers and SketchMonkey | Never calls SketchMonkey or external services itself |
| cad_get_evidence_schema | not checked | Manufacturing recommendations schema | No inspection result |
| cad_get_configurator | not checked | `Param.*` schema, parts, joints, BOM and pinned CDN URLs for the Three.js runtime, from code or a saved modelId | — |
| cad_compare_revisions | not checked | Parameter/size/volume/mass/part/check deltas between two scripts or saved revisions, plus an overlay PNG | — |
| cad_export_drawing | not checked | Dimensioned A4 drawing (front/top/right, isometric, ISO 7200 title block) as PDF, SVG or DXF | — |
| cad_export_model | account | Builds, measures and writes a downloadable file: `stl`, `stl-fins` (breakaway support fins baked in), `stl-fins-only`, `step`, `glb`, `zip` (per-part STLs + BOM); returns a download URL. 30/hour, 150/day | No gallery record; not a manufacturing certification |
| cad_save_model | account | Saves an editable script-cad model with revision history and a binary STL to the gallery; returns modelId, revision, STL URL and workbench link. 20/hour, 100/day | Not an order, payment or approval |
| cad_import_model | account | Imports STEP/STL/GLB (public HTTPS URL or base64 ≤ 20 MB) as private reference geometry for `importedModel(id)`; returns bounds and bodies; can delete on request | — |
| cad_list_models | account | Owned CAD scripts and parameter values | — |
| cad_save_feature / cad_list_features | account | Reusable `defineFeature` / `lib.mine.<name>` features in the private library | Cross-account sharing gated |
| cad_add_review_comment / cad_list_review_comments | account | Design-review comments pinned to an owned saved model revision, part or 3D point | — |
| cad_publish_configurator | account | Builds and publishes a live configurator at `https://www.3dj.app/configurator/<id>` | — |
| openscad_get_starters | public | Three editable OpenSCAD examples and language rules | — |
| openscad_compile_model | account | Compiles with the real isolated OpenSCAD/Manifold engine: effective source, parameters, triangle count, closed-mesh measurements, optional axis-aligned build-volume fit. 24 KB source, 20/hour, 100/day; external files, libraries and fonts refused | No STL download, gallery record, approval or printer command |
| list_providers | account | Provider health and generation allowance | — |
| generate_from_text / generate_from_image_url | account | Start asynchronous mesh generation (image must be a public HTTPS URL) | A started job is not a finished model |
| get_generation_status | account | Poll an owned generation and retrieve its result URL | — |
| list_my_models / get_model_download_url | account | Owned gallery models and their actual stored asset URL | A GLB is not automatically an STL |
| get_account_status | account | Account connection, saved-model count, `printQuoteRequestsOpen` | — |
| request_print_quote | account | Submit a saved-model brief for operator review; returns request ID and status | No price, order, payment or booking |
| list_print_requests / cancel_print_request | account | Own review requests and operator notes; cancel an own review request | Not an order cancellation or refund |
| list_print_quotes | account | Own operator-issued EUR quotes and inspection attestations | The tool does not verify the file hash itself |
| accept_print_quote | account | Record explicit acceptance of exact quote terms (`quoteId`, `quoteHash`) | No payment, booking or dispatch |

No tool for payment, paid order creation, printer dispatch, shipping or tracking was advertised. The 3DJ description itself states that measurements are geometry diagnostics, not structural or safety certifications, and that print readiness still requires slicer inspection and a physical prototype.

## Historical baseline — 2026-10-11

Live `tools/list` then exposed 16 tools (the CAD starters, validate and evidence-schema tools; generation, gallery, account and print-quote tools). At that time `cad_validate_script` performed syntax and parameter inspection only, and `openscad_get_starters` / `openscad_compile_model` were in an open draft PR (NeuralDEEPnet/3dj#2) and absent from the live catalogue. Missing credentials were rejected with JSON-RPC -32001 for the account tools, which verified authentication refusal, not successful account use. Source references: NeuralDEEPnet/3dj commit 50f52894 (baseline), 28bb466e (restored main), PR #1 (print requests and quotes).

Skill text that describes a tool's behaviour follows the most recent observation above; if the live description disagrees, the live description wins and this file should be updated with the date.
