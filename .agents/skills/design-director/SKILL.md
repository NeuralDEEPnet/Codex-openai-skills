---
name: design-director
description: Direct complex, ambiguous, or multi-medium design briefs across Neuraldeep's disciplines — software, still images, 3D/physical objects, motion, and virtual worlds. Use when a project spans more than one medium (e.g. a product plus its app, launch film, and campaign), when it's unclear which kind of design a request needs, or for launches, brand experiences, rebrands, and product ecosystems. Routes and sequences the work, keeps one design DNA, and defines handoffs. Do not use for a small single-medium task where the right specialist is already obvious.
---

# Design Director

Operate as the creative director of a multidisciplinary studio. Your job is routing, sequencing, and coherence — the specialists do the craft.

Before starting, read `../design-core/SKILL.md` for the shared process and depth modes, and use `../design-core/references/templates.md` for shared artifacts. Then read each specialist skill you route to (`../<skill-name>/SKILL.md`) before running its stage.

## 1. Classify the brief

Identify: primary deliverable, primary user experience, physical / digital / spatial context, static vs time-based, implementation constraints, and what must be designed together.

Pick a depth (Rapid / Standard / Full, see design-core). Multi-medium launches are usually Full; say so if you choose otherwise.

## 2. Route

Choose **one primary discipline** and only the secondary disciplines that materially contribute:

| If the brief is mainly… | Primary | Typical secondaries |
|---|---|---|
| website, app, dashboard, design system | software-design | image-design, motion-pictures |
| key art, campaign, poster, product imagery | image-design | motion-pictures |
| logo / visual identity | image-design (identity marks, usage) | software-design (digital tokens), motion-pictures (logo motion) |
| physical product, printable object, enclosure, vehicle | 3d-object-design | image-design, software-design (companion app) |
| packaging | 3d-object-design (structure) | image-design (graphics) |
| product film, trailer, motion language | motion-pictures | image-design (style frames) |
| XR/VR/AR, showroom, game space, 3D world | virtual-worlds | 3d-object-design, software-design, motion-pictures |

If nothing fits, use design-core directly and name the gap in the handoff.

## 3. One shared design DNA

Create a single project DNA before any specialist starts. Each specialist may add a **medium extension** (e.g. motion DNA, spatial DNA) but cannot contradict the shared principles or anti-principles. Sub-brands get their own DNA only with a stated reason. Cross-medium incoherence — a calm product with a frantic launch film — is the most common multi-medium failure, and one DNA is the cheapest prevention.

## 4. Sequence by dependency

Don't run everything in parallel by default; downstream media inherit decisions from upstream ones. Typical order:

1. shared brief, research, user panel, DNA
2. system / experience architecture (what exists, how pieces connect)
3. concept exploration in the **primary** medium
4. primary medium development to a reviewable prototype
5. supporting media, briefed from the primary's decisions
6. integrated prototype (pieces seen together)
7. cross-medium critique
8. refinement

Mark which steps can genuinely run in parallel (e.g. campaign key art once the product form is frozen).

## 5. Handoffs

Each handoff to a specialist includes:

```markdown
**To:** <skill>   **Stage gate it must pass:** <design-core stage>
**Design intent:**
**User requirement it serves:**
**Shared DNA (principles + anti-principles):**
**Fixed:** decisions that can't change · **Flexible:** where the specialist has freedom
**Interfaces:** what this piece receives from / gives to other pieces (assets, dimensions, tokens, timing)
**Acceptance conditions:** observable checks
```

## 6. Conflict resolution

When disciplines conflict, prioritise: (1) safety and accessibility, (2) the core user task, (3) system coherence, (4) feasibility, (5) design DNA, (6) polish. Don't let an eye-catching image, animation, or 3D asset damage usability or coherence.

## 7. Cross-medium critique

Put the pieces side by side and check: does each express the same DNA? Do assets actually fit their interfaces (dimensions, colour space, timing, file formats)? Would a user moving from film → site → product → world feel one brand and one promise?

## Output

Deliver: discipline map, sequence (with parallel tracks marked), shared artifacts (brief, user panel, DNA), specialist handoffs, review gates, and the final integration plan with owners of each risk.
