---
name: interactive-3d-print-design
description: Turn customer-adjustable 3D printing ideas into industrial-design directions, parametric CAD briefs, inspectable geometry and production-aware handoffs for the 3DJ workflow.
---

# Interactive 3D-print product design

Use for configurable printed products, acoustic tiles, modular wall panels, lamps, robot shells, accessories and printable spare parts. Run the core industrial-design process from `3d-object-design`; this skill adds parameter/interaction design and CAD handoff.

1. Establish user and market scenario plus dimensional envelope, printer, materials, intended attachment, tolerances, service life and physical interactions.
2. Propose two or three structurally distinct concepts; explain silhouette, primary sections, material finish, continuity, assembly and feature priority. Variants should be meaningfully different, not arbitrary patterns.
3. Map each user-visible knob to an actual CAD parameter, with a bounded validated range: form family, footprint X/Y, relief Z, contour count, corner radius, wall thickness, joint tolerance, mount options, material and finish. Check coupled dependencies; don't allow a slider to violate print bed or leave a wall thinner than the process assumption.
4. The UI may show a conceptual **2D projection** of parameter states, but label it as such. True rotate/zoom, parameter updates, STL/STEP export and slicing require an actual 3D viewer/CAD engine and wired export actions. Never suggest a sketch preview is verified production geometry.
5. Hand off the selected design DNA and exact parameters to 3DJ parametric-printable-surfaces (if available), otherwise supply executable OpenSCAD or CAD source and validate with a local engine before saying 'exported'. Require front/back/isometric previews **from the exported geometry**, separate printable STL/3MF, editable source, printer-fit report, and a prototype test plan.
6. For functional 'acoustic' claims, rigid printed relief alone does not establish sound absorption. Specify real felt/foam/perforation/air-gap construction and measurement, or label the part a decorative/diffuser-style panel.
7. For four-way keyhole mounting, show all orientations, hidden entry path, screw-head pocket, shaft passage, retaining lip, edge clearance and local unsupported bridge. Specify provisional fastener interfaces and print-fit coupon before production.

**Initial demo:** 160 × 160 × 24 mm PETG quad tile with six surface contours and 19 mm sculptural relief, four rear mount directions. Source example may be taken from the standalone OpenSCAD template in the companion 3DJ skill.

**Outputs:** design brief → alternative concepts → selected parameters → actual editable source → verified mesh → real model views → print/fitting risk log. No claims of completed orders/print dispatch without tool confirmation.
