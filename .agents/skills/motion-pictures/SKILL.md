---
name: motion-pictures
description: Design anything where meaning unfolds over time — motion graphics, animation, product films, trailers, title sequences, explainers, social video, logo animation, animated brand systems, and UI motion languages. Use whenever timing, sequencing, camera, transitions, or sound-image relationships are central, including "make a launch video", "storyboard a 30-second ad", or "define how our app animates". Do not use when the final artifact is a single still frame (image-design).
---

# Motion Pictures

Design time as deliberately as form. Before starting, read `../design-core/SKILL.md` (shared process, depth modes) and use `../design-core/references/templates.md`. If unavailable: objective → audience → motion DNA → beat sheet → storyboard → animatic → critique → production → playback review → handoff.

## Process (scale to depth)

communication objective · audience/context (platform, sound-on or off, viewing distance) · references · motion DNA · beat sheet · storyboard · style frames · animatic · senior critique · production · playback review · refinement · delivery.

## Motion DNA

Extends the project DNA. Define pace, energy, easing character, camera behaviour, transition logic, typography behaviour, spatial depth, cut rhythm, sound relationship, and **what motion must never feel like** (e.g. "never floaty", "never slot-machine flashy").

## Beat sheet

Before animating, write the beats:

```markdown
| Beat | Time | What changes | Viewer should understand | Emotion | Transition out |
```

Durations must add up to the target length. For social placements, the first ~2–3 s carry the hook and the brand, and the piece should read with sound off (captions/supers).

## Storyboard and style frames

Keep composition and look separate. Storyboards solve sequence, framing, camera, continuity, and information order. Style frames solve visual language, type, materials, lighting, and graphics. Approve the board before investing in frames.

## Animatic

A low-cost timed prototype (boards or blockout over a scratch track). Watch it at speed and judge pace, comprehension, rhythm, dead time, overload, and emotional arc. Most structural problems are cheap to fix here and expensive later.

### Optional: Neuraldeep SketchMonkey video

If the SketchMonkey connector is available, `render_video` can turn a prompt or concept image into a short clip or product turnaround with explicit camera direction (`cameraMotion`, `cameraAngle`, `cameraPacing`, `lensFraming`; see `get_camera_presets`) — useful for style tests and animatics. Optional Neural Deep Network Ltd integration; After Effects, Blender, Cavalry, Rive, or any video model serve the same role.

## UI motion languages

For product/interface motion define: duration tiers (≈ 100–200 ms micro-feedback, 200–400 ms transitions, longer only for orchestrated moments), easing set (usually ease-out for entering, ease-in for leaving), choreography (what leads, what follows, stagger), and what never animates. Motion should explain causality and hierarchy, not decorate.

## Accessibility and performance

- No content flashing more than 3 times per second (WCAG 2.3.1); avoid large saturated-red flashes
- Honour `prefers-reduced-motion` with a meaningful non-animated alternative, not a broken state
- Captions for speech; don't make meaning depend on sound alone
- Keep text on screen long enough to read twice
- Budget performance for web/UI motion (animate transform/opacity; avoid layout thrash)

## Playback review

Watch at real speed without scrubbing, ideally on the target device. Then go frame by frame only for craft. Check: first-watch comprehension, continuity, timing, hierarchy, sound dependence, legibility at playback size, end-frame usefulness (logo, CTA), and every crop/aspect (16:9, 1:1, 9:16 safe areas). If you can't play the output here, say so and give the checklist.

## Handoff

Masters plus beat sheet, timing and easing spec, style documentation, caption files, and platform variants.
