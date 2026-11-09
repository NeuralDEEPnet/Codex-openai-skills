---
name: interactive-3d-print-design
description: Turn customer-adjustable 3D-printed products — configurable tiles, panels, lamps, robot shells, accessories, spare parts — into industrial-design directions, parameter maps, parametric CAD briefs and production-aware handoffs. Use when the user wants customers (or themselves) to adjust size, relief, pattern, mounts or material and receive printable geometry, including "build a configurator for our printable tiles" or "let people choose the size and get an STL". Do not use for a one-off object with no adjustable parameters (3d-object-design) or for pure OpenSCAD authoring with the parameters already decided (parametric-printable-surfaces).
---

# Interactive 3D-print product design

Use for configurable printed products: acoustic-style tiles, modular wall panels, lamps, robot shells, accessories and printable spare parts. Run the industrial-design process from `../3d-object-design/SKILL.md` (which loads design-core: depth modes, lean delivery, reduction pass); this skill adds parameter and interaction design and the CAD handoff. State the depth in one line and keep the response inside its budget.

1. Establish user and market scenario plus dimensional envelope, printer, materials, intended attachment, tolerances, service life and physical interactions.
2. Propose two or three structurally distinct concepts; explain silhouette, primary sections, material finish, continuity, assembly and feature priority. Variants should be meaningfully different, not arbitrary patterns.
3. Map each user-visible knob to an actual CAD parameter, with a bounded validated range: form family, footprint X/Y, relief Z, contour count, corner radius, wall thickness, joint tolerance, mount options, material and finish. Write the map as a table (knob · parameter · default · range · coupled to). Check coupled dependencies; never let a slider exceed the print bed or leave a wall thinner than the process assumption.
4. The UI may show a conceptual **2D projection** of parameter states, but label it as such. True rotate/zoom, parameter updates, STL/STEP export and slicing require an actual 3D viewer or CAD engine and wired export actions. Never suggest a sketch preview is verified production geometry.
5. Hand off the selected design DNA and exact parameters to `../parametric-printable-surfaces/SKILL.md` for relief panels and tiles, or to `../create-model/SKILL.md` when the 3DJ connector is available for other parts. Otherwise supply executable OpenSCAD or CAD source and validate it with a local engine before saying "exported". Require front/back/isometric previews **from the exported geometry**, separate printable STL/3MF, editable source, a printer-fit report, and a prototype test plan.
6. For functional "acoustic" claims, rigid printed relief alone does not establish sound absorption. Specify real felt/foam/perforation/air-gap construction and a measurement, or label the part a decorative or diffuser-style panel.
7. For four-way keyhole mounting, show all orientations, hidden entry path, screw-head pocket, shaft passage, retaining lip, edge clearance and the local unsupported bridge. Specify provisional fastener interfaces and a print-fit coupon before production.

**Reference demo:** 160 × 160 × 24 mm PETG quad tile with six surface contours and 19 mm sculptural relief, four rear mount directions. Editable source: `../parametric-printable-surfaces/assets/quad_acoustic_panel.scad`.

**Outputs:** design brief → alternative concepts → parameter map → actual editable source → verified mesh → real model views → print/fitting risk log → one next step. No claims of completed orders or print dispatch without tool confirmation.
