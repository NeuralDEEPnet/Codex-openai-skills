---
name: print-production
description: Prepare a 3D model for printing by Neural Deep Network through the 3DJ connector — manufacturing requirements, mesh and fit gates, print-quote requests, operator quotes and explicit acceptance — and explain quote, checkout and shipping readiness accurately. Use for "get this printed", "request a print quote", "is my model ready to manufacture", or "what does the quote say". Do not use for designing or modelling the part (3d-object-design, create-model), for generic slicer or printer troubleshooting, or to imply payment, booking or shipment that no tool performed.
---

# Print and deliver

Discover the actual MCP catalogue before proceeding. Read `../create-model/references/capabilities.md` for the tools observed so far and their limits. Do not assume a source change has been deployed. Never claim an order, charge, print booking, dispatch or shipment happened without its own supported action and confirmed result. Lean delivery applies: lead with the readiness status, then the gaps, then one next step.

Collect or derive: exact model/version, units, target dimensions, material preference, colour, quantity, intended use, tolerances, finish, and delivery country/postal region. State unknowns explicitly. Do not collect a full delivery address or card data in chat; these belong in secure checkout when it exists.

When `openscad_compile_model` or `cad_validate_script` is discovered, use its measured bounding box and mesh checks as supporting evidence for the design brief. Record the supplied printer volume and fit limitations. A compilation or validation has no exported asset; `cad_export_model` or `cad_save_model` produces the inspected file. Export and save the actual file before requesting a quote that requires a saved model. Never turn `manufacturingApproved: false` into an approval.

Separate three gates:

- **Design:** functional dimensions and model revision approved by the user.
- **Manufacturing:** a real exported mesh or solid inspected for watertightness, topology, thin walls, build volume, supports and assembly clearance; printer- and material-specific checks and an operator review. Schema, syntax and validation tools report diagnostics; they do not pass this gate on their own.
- **Commercial:** a server-generated, expiring quote tied to the inspected file hash, quantity, material/finish, destination, currency, taxes and shipping. Show total and lead time before sending the user to verified checkout. Never estimate prices or delivery promises as if they were a live quote.

If `get_account_status` and `request_print_quote` are discovered, check account status and `printQuoteRequestsOpen`. When enabled and the user requests submission, collect the required brief and choose the user's completed saved model. Use one unique requestKey for the brief, retain it for identical retries, and create a new key after any brief or model changes. Pass only fields accepted by the discovered schema. Submit with `request_print_quote`, then report the returned request ID and status. A request asks an operator for a quote; it is not a priced quote or manufacturing approval. The sourceRevision identifies stored source metadata, not an inspected file-byte hash.

Use discovered `list_print_requests` for history and returned review notes. Use `cancel_print_request` only when the user asks to cancel the named request. This cancels a review request; it is not an order cancellation or refund. If tools are absent, account connection fails or requests are closed, return a concise draft brief with missing requirements and status `awaiting manufacturing review and quote`.

When `list_print_quotes` is discovered, show the user's issued quote with confirmed material, colour, quantity, dimensions, delivery region, item price, shipping, tax, EUR total, expiry and lead time after payment and approval. Show the operator's inspection note and file reference; explain that the tool records an operator attestation and does not itself inspect geometry or verify the file hash. Treat expired, invalidated or superseded quotes as unavailable. Never invent a price.

When the user explicitly accepts those exact terms and `accept_print_quote` is discovered, pass the quote's returned id as quoteId and the exact returned quoteHash. If it fails due to expiry or changed review, retrieve current quotes and explain the reason. Report the returned acceptance without implying a payment, print booking or shipment. Checkout is not connected by this release.

Do not invent checkout links. For future connected commerce, use only returned URLs and order IDs, get explicit acceptance of the actual quote, and let the payment provider and server confirm payment. Refunds, paid-order cancellations and printer dispatch require their own supported actions.

Before printing functional parts, identify loads, heat, outdoor exposure, moisture and assembly needs. Use material-specific limits supported by the operator. Recommendations are provisional until the actual geometry and process have been inspected. Offer iteration instead of claiming every generated model is printable.

**Without the connector:** deliver the three-gate checklist filled in from what the user supplied, the mesh checks they can run (`trimesh` on the file bytes, slicer preview), and the status `awaiting manufacturing review and quote`. Any print bureau can take the same brief.
