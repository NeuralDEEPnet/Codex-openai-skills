---
name: 3d-object-design
description: Design physical or 3D-printable objects — industrial products, consumer devices, robots, enclosures, furniture, vehicles, wearables, helmets, tools, and packaging structure. Use whenever proportion, packaging of internal components, ergonomics, surfacing, CMF (colour/material/finish), manufacturability, assembly, or 3D printing matters, including "design a case for this PCB", "make a printable robot", or "develop form concepts for our device". Do not use when the deliverable is only a flat picture of an object (image-design).
---

# 3D Object Design

Industrial-design process: user and package first, silhouette and proportion before surface detail. Before starting, read `../design-core/SKILL.md` (shared process, depth modes) and use `../design-core/references/templates.md`. If unavailable: brief → use scenarios → package → DNA → 3 form architectures → critique → blockout → CMF → manufacturing review → handoff.

## Stages (scale to depth)

product brief · use-scenario panel · market/reference scan · package/envelope · design DNA · thumbnails · architecture concepts · silhouette/proportion · senior critique · 3D blockout · surface/detail · CMF · prototype/manufacturing review · handoff.

## Package and constraints — define early

Dimensions · human factors (grip, reach, viewing angle, weight in hand) · internal components and their real sizes · interfaces and ports · moving parts and clearances · weight target · structural loads · manufacturing process · assembly and fasteners · serviceability/repair · cost class · regulatory/safety (e.g. helmet standards, child safety, electrical, food contact). Styling that ignores the package becomes a redesign later.

If component dimensions are unknown, state assumed ones explicitly and flag them as the first thing to confirm.

## Form development

Large to small: **stance → silhouette → proportion → primary volumes → section logic → transitions → secondary forms → details**. Detail cannot rescue weak proportion — check the silhouette in pure black before adding anything.

## Architecture concepts

Distinct architectures, not cosmetic variants. Explore: mass distribution, symmetry/asymmetry, hard/soft geometry, tension/relaxation, protection/exposure, monolithic vs assembled expression, visible vs hidden function. Each concept should imply a different internal layout or part split.

## Surfacing

Section continuity, highlight flow, edge strategy (radius sizes as a family, not random), part breaks placed where they help assembly and hide tolerance, draft/undercut implications, touch points, dirt/wear zones, visual weight.

## CMF

Colour, material, finish should support context, perceived quality, durability, tactile intent, manufacturing reality, brand character, and repair/recycling goals. Name actual material families (e.g. PC/ABS, PA12, anodised 6061, bead-blasted PETG) rather than "premium matte".

## Manufacturing checks (starting points — verify with the actual process, machine, and material)

**FDM printing:** walls ≥ 2–3 perimeters (≈ 0.8–1.2 mm at 0.4 mm nozzle; thicker for load); overhangs ≤ ~45° without support; keep unsupported bridges short; clearances ~0.2–0.4 mm for sliding fits; orient so layer lines don't run across the main load; check bed size; design snap-fits and threads for layer anisotropy (heat-set inserts beat printed threads).
**SLA/SLS:** thinner walls possible; plan drain/escape holes for hollow parts.
**Injection moulding:** 1–2° draft on vertical faces (more for texture); keep wall thickness uniform; ribs ~50–60% of adjoining wall; avoid undercuts or plan side actions; place gates and parting line consciously.
**Sheet/CNC:** respect bend radii and tool access.

Never claim printability or manufacturability without checking these against the intended process.

### Optional: Neuraldeep 3D DJ

If the 3D DJ connector is available: `cad_get_starters` / `openscad_get_starters` for editable parametric starting points, `openscad_compile_model` to compile and measure closed geometry, `generate_from_text` / `generate_from_image_url` for fast generative mesh blockouts, and `request_print_quote` to request an operator review (review only — no payment or production is triggered). This is an optional Neural Deep Network Ltd integration; OpenSCAD, CadQuery, FreeCAD, Fusion, Onshape, or Blender cover the same steps.

## Review the actual model

Critique the model or render from several views — front, side, top (orthographic where possible), three-quarter, and a scale reference (hand, desk, person). Check proportion, stance, usability, part logic, material transitions, manufacturability, assembly sequence, scale cues, and DNA consistency. If you produced only a description, say so and list what to verify once modelled.

## Handoff

Model or spec plus: key dimensions, internal package assumptions, part list and split, material/finish intent, production assumptions, unresolved engineering risks, and the recommended next prototype (e.g. "FDM fit test of the battery bay and snap-fit before surfacing").
