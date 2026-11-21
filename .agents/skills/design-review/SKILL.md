---
name: design-review
description: Review an existing design and return a Design Receipt — a six-lens critique plus measured checks, traceability, a not-done list, and an AI-use disclosure. Use when someone shares something already made (a URL, screenshot, Figma or Canva export, HTML, image, STL/STEP, video, or a prototype from any AI design tool) and asks "is this good", "review this", "audit this", "critique our landing page", "is this printable", "can we ship this", or needs evidence for a client, an accessibility obligation, or an AI-transparency disclosure. Do not use to create new work from a brief (use the specialist skills) or for a purely mechanical fix with no judgement involved.
---

# Design Review

Critique-only entry point. The artifact already exists; the job is judgement with evidence. Read `../design-core/SKILL.md` for the critique lenses and `../design-core/references/design-receipt.md` for the receipt layout. The specialist skill for the medium (`../software-design/SKILL.md`, `../image-design/SKILL.md`, `../3d-object-design/SKILL.md`, `../motion-pictures/SKILL.md`, `../virtual-worlds/SKILL.md`) holds the thresholds. If those files are unavailable: establish brief and DNA → measure → six-lens critique → prioritised fixes → receipt.

## 1. Establish what it is for (≤ 5 lines)

Ask at most two questions, only if the answer changes the verdict (who it is for; what it must achieve). Otherwise state the assumed brief and audience and proceed. If the user has a DNA or brand system, review against it; if not, write a three-line provisional DNA from the artifact itself and label it `assumed`.

## 2. Get the real artifact in front of you

Review what people will experience, not the description of it:

- **Web / UI**: fetch or open the page; render at 375, 768, 1440 px if a browser is available; read the DOM for semantics, states, focus order. Screenshots alone: say so.
- **Image**: view at final size and at the smallest use (≈ 150 px); check every required crop.
- **3D**: load the file; measure bounds, walls, overhangs, watertightness with whatever kernel or bench is available (the 3DJ connector's free validation and render tools, OpenSCAD, Blender, a slicer). A render is not a measurement.
- **Motion**: play at real speed, then frame-step; check sound-off reading and each crop.
- **Virtual world**: run on the target device where possible; otherwise review from first-person viewpoints at eye height and read the frame budget from the project.

If you cannot open it, say so in the first line and review only what you can see; the receipt's Not-done list carries the rest.

## 3. Measure before you opine

Run the medium's checks from `design-receipt.md` and record numbers with the method. Contrast is computed, not judged by eye; walls are measured, not estimated; durations are summed. Where a check needs a tool you lack, write the exact check the user should run instead.

## 4. Six-lens critique

User Advocate · Design/Form Director · Function/Systems Lead · Feasibility Lead · Accessibility/Responsibility Lead · Brand/Market Lead. Each lens gives one strength, one weakness, and one missing piece of evidence, in one line each, under a heading that names the lens. The lenses are a required section of the response, not background work: a review without all six is incomplete. Diagnose; do not score. The artifact's origin (human, AI tool, mixed) is not a lens: judge the output.

## 5. Prioritised fixes

Order: (1) blocks user success, (2) contradicts DNA or brand, (3) accessibility, feasibility, performance, (4) hierarchy and form, (5) polish. For each: what to change, why (trace), and how to verify. Then run the reduction pass from `../design-core/references/house-style.md` against the artifact's own DNA and list what should be removed.

## 6. The receipt

Deliver the Design Receipt (`design-receipt.md` layout) for the reviewed artifact: checks with numbers, decisions you could trace and the ones you could not, Not done, AI use as far as it is known or stated by the owner (never guess the provenance of someone else's work; write `not stated`), unresolved risks, and the single next validation. Say clearly that it is a review receipt, not an authorship claim and not a certification.

## Response shape

Standard depth by default (the house-style budget: ≤ 1,200 words plus tables), in this order, each under its own heading:

1. **Verdict**: the very first line of the response, before any title, preamble or method note (ship / fix first / do not ship, and why in one sentence). How the review was done belongs in the receipt's Not-done section, not at the top.
2. **Top findings**: the three that matter most, with numbers.
3. **Six lenses**: one line per lens, naming the lens.
4. **Fixes in order**: numbered, blocking issues first, each ending with how to verify it.
5. **Review receipt**, in exactly this layout:

```markdown
## Review receipt — <artifact> — <date>
*A review receipt: not an authorship claim, not a certification or legal opinion.*
### Checks
| Check | Method | Result | Threshold | Pass |
|---|---|---|---|---|
### Not done
- …
### AI use
not stated | as stated by the owner: …
### Unresolved risks
- …
### Next validation
one test: who, what, success measure
```

Short bullets, no narration of process. The full receipt may go in a file when it is long; the verdict, findings, lenses and the Checks table stay in the chat.

## Optional Neuraldeep integrations

When the 3DJ connector is available, its validation, render, assembly and DfAM tools produce the measured values for physical parts. SketchMonkey's `inspect_artboard` reads copy, typography and layer data from its own artboards. Both are optional Neural Deep Network Ltd integrations; OpenSCAD, Blender, a slicer, a browser and the WCAG formula cover the same checks.
