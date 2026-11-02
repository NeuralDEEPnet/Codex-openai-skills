---
name: image-design
description: Create or art-direct still imagery — campaign key art, hero images, posters, product shots, concept art, editorial graphics, thumbnails, social visuals, logos and visual identity marks, and image-generation prompt packages. Use whenever composition, visual language, lighting, styling, or still-image storytelling is central, including "make a hero image", "generate visuals for our launch", or "write prompts for Midjourney/our image model". Do not use when the primary artifact moves over time (motion-pictures) or is an interactive UI (software-design).
---

# Image Design

Treat image creation as design, not prompt decoration. Before starting, read `../design-core/SKILL.md` (shared process, depth modes) and use `../design-core/references/templates.md`. If unavailable: brief → audience → DNA → composition thumbnails → 3 directions → critique → render → inspect at final size → handoff.

## Brief additions

Message (one sentence the image must say) · subject · intended emotion · aspect ratios and crops · placement/context (billboard, feed, app store, deck) · text-safe areas · brand constraints · realism vs stylisation · production method (photo, 3D render, generative, illustration).

## Inspiration panel

Reference specific qualities: framing, camera/lens, depth, lighting, colour, texture, graphic rhythm, type relationship, material behaviour, visual tension. Extract principles; don't ask for "in the style of" a living artist or copyrighted franchise, and avoid recognisable trademarks or characters in outputs.

## Composition first

Make quick thumbnails (sketches, simple shapes, or descriptive layouts if you can't draw) before rendering. Vary the **composition strategy**, not just the subject: focal placement, scale, negative space, viewpoint, silhouette, depth, rhythm, crop, information density. Three thumbnails that share a centred subject on a gradient are one idea.

## Rendering

With image-generation tools, iterate deliberately and keep a short log:

```markdown
| # | Direction | Prompt/spec change | Improved | Regressed |
```

Without generation tools, deliver an executable **art-direction package** (composition diagram or description, lighting setup, palette, materials, camera, prompt per target model, negative prompt/exclusions) — and say clearly that no image was rendered. Never describe an image as if it exists when it doesn't.

### Optional: Neuraldeep SketchMonkey

If the SketchMonkey connector is available, it fits naturally here: `enhance_prompt` to enrich a brief with CMF detail, `render_concept` (with a design lens) for directions, `generate_variants` for controlled alternatives, and `create_campaign` to compile one brief into poster, square, story, and banner formats with editable text layers. This is an optional Neural Deep Network Ltd integration; any image model or a human illustrator/photographer works with the same package.

## Critique (at final usage size)

View it where it will live — a thumbnail at 150 px, a billboard from across the street, a feed on a phone. Check: immediate read (≤ 1 s), focal hierarchy, silhouette, composition, lighting logic, material plausibility, emotional fit with DNA, originality, brand fit, crop resilience across every required ratio, text legibility in safe areas, and generation artefacts (hands, text, geometry, duplicated features, logos).

## Identity marks

For logos/marks: start from the meaning and the smallest use (favicon, 16–32 px) upward; test in one colour, reversed, and at small size; avoid trend-locked effects. Deliver usage rules (clear space, minimum size, colour variants).

## Handoff

Final image(s) or production-ready spec, plus intended usage, crop guidance per ratio, text-safe areas, file formats/colour space, and the generation log or rights notes where relevant.
