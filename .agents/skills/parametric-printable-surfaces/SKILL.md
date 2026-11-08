---
name: parametric-printable-surfaces
description: Design, iterate and verify parametric relief panels, 3D-printed tiles, patterns and wall products in OpenSCAD or code-CAD, with editable source, individual STL exports, mesh checks from the file bytes and four-way keyhole mounting checks. Use for "parametric wall tile", "relief panel in OpenSCAD", "generative hex tiles for printing", or any repeatable printed surface with real millimetre dimensions. Do not use for the customer-facing configurator and parameter mapping (interactive-3d-print-design), for decorative text-to-mesh generation (create-model), or for quoting and production (print-production).
---

# Parametric printable surfaces / 3DJ

Use for repeatable generative 3D panels, tiles, decorative acoustic-style reliefs, wave surfaces, organic reliefs or modular 3D-printable design. This extends `../create-model/SKILL.md` and `../print-production/SKILL.md`: read them when their tools or gates are needed, and `../3d-object-design/SKILL.md` for the design process (depth modes, lean delivery and the reduction pass come from design-core). Never assume a connected MCP tool exists: discover and verify the live 3DJ tool catalogue before invoking an endpoint.

## Design-to-STL contract

1. Capture or infer a **brief**: use case, printable width/height/depth in mm, material, target machine build volume, number and direction of contour features, mount/assembly strategy, whether sound absorption is required.
2. Build distinct form families (quad, hex, tri or flow), with a named design DNA and explicit manufacturability trade-offs. Preserve real physical dimensions and editability. For metric objects, prefer code-parametric OpenSCAD or CAD source, not text-to-mesh generation.
3. Model as one printable solid or a purposeful assembly. Define thicknesses, connectivity, orientation, pockets, clearances and relief height unambiguously. Provide a numerical default and a practical parameter range. Work from silhouette to section profiles to fine relief; do not let a render substitute for geometry.
4. Use the available actual CAD engine: when `openscad_get_starters` / `openscad_compile_model` are *live*, call them for compile and measurement. If unavailable or unauthenticated, a locally installed OpenSCAD can render and export source + STL when a coding runtime is present; otherwise return editable source without claiming an exported file. For source-only work, state the limitation in one line.
5. Verify an exported STL *from its bytes*, using the equivalent of `trimesh.load_mesh`, `is_watertight`, `is_winding_consistent`, `body_count`, `volume`, and bounding-box measurements. Evaluate print orientation, overhangs, bridges, minimum walls, assembly/fastener fits, and build-envelope margin separately. A manifold mesh is **not** a manufacturing approval. Preview front, back and at least one isometric view from the actual model.
6. Offer separate named outputs: `.scad` or other editable source, `.stl`, a front/back preview, print notes, and validation evidence. Never call a decorative render a downloadable STL. ZIP only as an optional extra.
7. For acoustic claims, rigid PETG panels by themselves are decorative or diffusive reliefs, **not verified sound absorbers**. If true absorption is requested, specify porous medium, effective air gap, mount scheme and a test protocol. Never invent NRC or absorption coefficients.

## Reference quad panel

See `assets/quad_acoustic_panel.scad` for fully editable standalone OpenSCAD source for a **160 × 160 mm quad**, **6 concentric ridges**, **19 mm relief**, **5 mm base** (24 mm overall), with four independent back-mounted keyhole orientations. Default target: Prusa MINI+ nominal 180³ mm, PETG. Use this as a starter, *not* a universally validated manufacturing design. The rear undercut lip requires a PETG bridging and fastener-fit test; print a small coupon before the panel. The inspection steps are in `references/print-verification.md`.

## Manufacturing gates

- CAD parameters established ≠ exported STL exists.
- Source compiles ≠ STL is watertight.
- Watertight STL fits bed ≠ support-free print, safe mount or tested acoustic treatment.
- For fasteners, ask for actual measured shaft/head dimensions before asserting mechanical compatibility.
- A slicer alone can estimate material and time; do not present unsliced numbers as measurements.

## Handoff

Lead with the files, then: parameters used and their ranges, what was compiled or measured and with what, what was not, the print orientation and the one coupon to print first. Brand when appropriate: Neural Deep Network Ltd · 3DJ · 3dj.app.
