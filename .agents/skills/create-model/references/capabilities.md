# Verified capabilities

Historical live baseline: NeuralDEEPnet/3dj commit 50f52894f4c31dfa5719f490b13d398d56d56924. Restored main: 28bb466e09ddd67f8654d706495f7ab6827663a7.
Live tools/list checked 2026-10-11 UTC: 16 tools discovered.
Endpoint: https://3dj-neuraldeepnet.on.adaptive.ai/api/mcp
Transport: stateless Streamable HTTP, POST JSON-RPC.

| Tool | Account key | Purpose |
| --- | --- | --- |
| cad_get_starters | No | Editable starter scripts and DSL reference |
| cad_validate_script | No | Syntax and declared parameters; no kernel execution |
| cad_get_evidence_schema | No | Manufacturing recommendations; no inspection result |
| cad_list_models | Yes | Owned CAD scripts and parameter values |
| list_providers | Yes | Provider health and generation allowance |
| generate_from_text | Yes | Start asynchronous mesh generation |
| generate_from_image_url | Yes | Start mesh generation from a public HTTPS image |
| get_generation_status | Yes | Poll owned generation and retrieve result URL |
| list_my_models | Yes | Owned gallery models |
| get_model_download_url | Yes | Actual stored asset URL |
| get_account_status | Yes | Account connection, saved-model count and request availability |
| request_print_quote | Yes | Submit a saved-model brief for operator review; no price or order |
| list_print_requests | Yes | Own review requests and operator notes |
| cancel_print_request | Yes | Cancel own review request; no refund or paid-order cancellation |
| list_print_quotes | Yes | Own operator-issued EUR quotes and inspection attestations |
| accept_print_quote | Yes | Record explicit acceptance of exact terms; no payment or booking |

The six account/request/quote tools are now advertised live. Missing credentials were rejected with JSON-RPC -32001 for get_account_status, list_print_requests, list_print_quotes and accept_print_quote. This verifies authentication refusal, not successful account connection, persisted requests, quote acceptance, or service availability. The operator-controlled request switch still requires a successful authenticated get_account_status check.

No tools for payment, paid order creation, printer dispatch, shipping or tracking were discovered. No embedded interactive MCP App view is bundled. Authenticated generation, gallery and commercial flows remain unverified.

## Deployed account and print-quote tools

The print-request implementation was merged in PR https://github.com/NeuralDEEPnet/3dj/pull/1. It adds `get_account_status`, `request_print_quote`, `list_print_requests` and `cancel_print_request`. These require an authenticated account; submission also requires the operator-configured service to be enabled. They save and track review requests, not priced quotes or paid orders. Only use these names when current live discovery exposes them. No checkout, printing or shipping tool is included.

The merged source also adds `list_print_quotes` and `accept_print_quote` for operator-issued EUR quotes and exact customer acceptance. Issuance is available only through the signed-in operator web queue; MCP cannot issue or change prices. The file reference, SHA-256 and inspection note are operator attestations, not independently verified by the service. Quote acceptance creates no payment or manufacturing booking. These names are present in the live catalogue on 2026-10-11. Successful authenticated execution has not been tested.

## OpenSCAD MCP source additions — deployment pending

`openscad_get_starters` supplies three editable examples and language rules without an account or computation. `openscad_compile_model` requires the caller's own account and uses the real isolated OpenSCAD/Manifold engine. It returns effective portable source, numeric parameters, triangles, closed-mesh measurements and optional axis-aligned build-volume fit. External files, libraries and fonts are refused. Limits: 24 KB source, 20 validations/hour and 100/day per account, two concurrent engine workers, 20-second engine timeout and 256 MB JavaScript heap per worker. These are validation allowances; no AI generation is called.

No STL asset URL, gallery save, manufacturing approval or printer command is created. Export an actual STL in the 3DJ OpenSCAD workbench. OpenSCAD does not provide STEP/B-rep export. Supports, brims, orientation optimization, wall strength and mechanical fit require further review.

Adaptive restored the real workspace `@neuraldeep/model-router` on main (28bb466e09ddd67f8654d706495f7ab6827663a7) and merged PR #1. Router tests and real OpenSCAD checks pass locally. These two new MCP tools are in open draft PR https://github.com/NeuralDEEPnet/3dj/pull/2 and remain absent from the live catalogue on 2026-10-11. Use only after discovery confirms deployment.
