---
name: parametric-printable-surfaces
description: Design, iterate and verify truly parametric relief panels, 3D printed tiles, patterns and wall products using OpenSCAD, with individual source/STL exports and four-way mounting checks.
---

# Parametric printable surfaces / 3DJ

Use for repeatable generative 3D panels, tiles, decorative acoustics, wave surfaces, organic reliefs or modular 3D-printable design. This extends the existing `create-model` and `print-production` skills: read them first when required. Never assume a connected MCP tool exists: discover and verify the live 3DJ tool catalogue before invoking an endpoint.

## Design-to-STL contract

1. Capture or infer a **brief**: use case, printable width/height/depth in mm, material, target machine build volume, number and direction of contour features, mount/assembly strategy, whether sound absorption is required.
2. Build distinct form families (quad, hex, tri or flow), with a named design DNA and explicit manufacturability tradeoffs. Preserve real physical dimensions and editability. For metric objects, prefer code-parametric OpenSCAD or CAD source, not text-to-mesh generation.
3. Model as one printable solid or a purposeful assembly. Define thicknesses, connectivity, orientation, pockets, clearances and relief height unambiguously. Provide a numerical default and a practical parameter range. Work from silhouette to section profiles to fine relief; do not let a render substitute for geometry.
4. Use the available actual CAD engine: when `openscad_get_starters` / `openscad_compile_model` are *live*, call them for compile/measurement. If unavailable or unauthenticated, a local installed OpenSCAD tool can render/export source + STL when a coding runtime is present; otherwise return editable source without claiming an exported file. For source-only work, state limitations.
5. Verify an exported STL *from its bytes*, using equivalent to: `trimesh.load_mesh`, `is_watertight`, `is_winding_consistent`, `body_count`, `volume`, and bounding-box measurements. Evaluate print orientation, overhangs, bridges, minimum walls, assembly/fastener fits, and build-envelope margin separately. A manifold mesh is **not** a manufacturing approval. Preview front, back and at least one isometric view from the actual model.
6. Offer separate named outputs: `.scad` or other editable source, `.stl`, a front/back preview, print notes, and validation evidence. Never call a decorative render a downloadable STL. ZIP only as optional extra.
7. For acoustic claims, rigid PETG panels by themselves are decorative/diffusive reliefs, **not verified sound absorbers**. If true absorption is requested, specify porous medium, effective air gap, mount scheme and a test protocol. Never invent NRC or absorption coefficients.

## Reference quad panel

See `assets/quad_acoustic_panel.scad` for fully editable standalone OpenSCAD source for a **160 × 160 mm quad**, **6 concentric ridges**, **19 mm relief**, **5 mm base** (24 mm overall), with four independent back-mounted keyhole orientations. Default target: Prusa MINI+ nominal 180³ mm, PETG. Use this as a starter, *not* a universally validated manufacturing design. The rear undercut lip requires a PETG bridging and fastener-fit test; print a small coupon before the panel.

## Manufacturing gates

- CAD parameters established ≠ exported STL exists.
- Source compiles ≠ STL is watertight.
- Watertight STL fits bed ≠ support-free print, safe mount or tested acoustic treatment.
- For fasteners, ask for actual measured shaft/head dimensions before asserting mechanical compatibility.
- A slicer alone can estimate material/time; do not present unsliced numbers as measurements.

Brand when appropriate: Neural Deep Network Ltd · 3DJ · 3dj.app.
