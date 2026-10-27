---
name: virtual-worlds
description: Design immersive and spatial experiences — VR, AR, mixed reality, WebXR, interactive 3D environments, virtual showrooms, social worlds, simulations, game spaces, digital twins, and persistent 3D ecosystems. Use whenever presence, scale, locomotion, spatial interaction, world rules, embodied UI, comfort, or real-time 3D performance matters, including "build a VR showroom", "design a metaverse space", or "make an AR learning experience". Do not use for a conventional 2D app with incidental 3D decoration (software-design).
---

# Virtual Worlds

Design the world as a system of space, behaviour, objects, interfaces, and time. Before starting, read `../design-core/SKILL.md` (shared process, depth modes) and use `../design-core/references/templates.md`. Coordinate with the other specialists (see "Cross-discipline calls"). If design-core is unavailable: brief → users → platform → DNA → world rules → journey → greybox → critique → comfort/performance review → handoff.

## Process (scale to depth)

experience brief · user/context panel · device/platform constraints · world references · spatial DNA · world rules · journey and encounter map · spatial thumbnails/greyboxes · interaction prototypes · senior critique · integrated prototype · comfort/performance/accessibility review · refinement · handoff.

## Experience model

Specify: single-user vs social · seated / standing / room-scale · inputs (controllers, hands, gaze, desktop, mobile touch) · persistent vs session · authored vs generative content · realistic vs stylised scale · core loop · entry and exit (including how people leave safely and fast).

## World rules

What the user can see, reach, move, manipulate, create, destroy, own, share, and remember. Coherence comes from predictable rules; write them as a short table and keep every interaction consistent with it.

## Spatial design

Landmarks, paths, districts/zones, thresholds, vistas, compression/release, scale hierarchy, orientation cues, social distances, quiet/safe areas. Navigation shouldn't depend on floating menus alone — people orient by landmarks and sightlines.

## Interaction

Prefer embodied, spatially legible interactions when they aid understanding. For each action define trigger, affordance, feedback (visual + audio + haptic where available), state, failure/recovery, and multiplayer implications (who sees it, who can interrupt it).

## Comfort and inclusion (starting points — verify against target platform guidelines)

- Locomotion: offer teleport and snap-turn (≈ 30–45°) by default; smooth locomotion optional with comfort vignette; never move the camera without user intent
- Seated mode and reach: keep core interactions within a comfortable arm's-length band and below shoulder height; support either hand
- Text: large, high-contrast, placed roughly 1–3 m away, world- or body-locked rather than head-locked
- Sensory load: avoid flicker, strobing, and sudden loud audio; give audio alternatives (captions, visual cues)
- Social worlds: personal-space bubble, mute/block/report, safe zones; design for harassment from day one
- Age-appropriate design and stricter defaults when users may be minors

## Performance budgets

Set targets per platform and design within them: frame rate (standalone headsets commonly 72–90 Hz → ~11–14 ms per frame; desktop/WebXR as specified), draw calls, triangle counts, texture memory, material/shader complexity, real-time lights, particles, animated characters, and networked entities. Use LODs, baked lighting, and instancing. A world that drops frames in VR causes discomfort, so performance is a comfort issue, not just polish.

## Cross-discipline calls

- 3d-object-design — hero objects and products in the world
- software-design — panels, menus, HUDs, account and settings flows
- motion-pictures — transitions, sequences, narrative beats
- image-design — key art, textures, visual targets, promotion

Optional: the Neuraldeep **3D DJ** connector can produce generative mesh or parametric blockouts for world assets (see 3d-object-design). Any DCC tool or asset library works equally well.

## Review at intended scale

Experience the world on the target device and scale where possible; otherwise review the greybox from first-person viewpoints at eye height (seated and standing). Check orientation, comfort, discoverability, spatial hierarchy, frame-time against budget, social behaviour, environmental storytelling, and DNA coherence. If you can't run it here, say so and provide the test plan.

## Handoff

World map, world-rules table, interaction model, asset hierarchy and budgets, UI/spatial rules, comfort settings, safety/moderation model for social spaces, unresolved risks, and validation plan (including a comfort test with first-time users).
