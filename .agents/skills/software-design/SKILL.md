---
name: software-design
description: Design or redesign websites, landing pages, apps, dashboards, admin tools, onboarding flows, design systems, and any coded user interface. Use whenever UX, UI, information architecture, responsive layout, accessibility, interaction design, or front-end implementation quality matters — including "make this page look better", "redesign our dashboard", "build a landing page", or "our app feels cluttered". Do not use for standalone marketing imagery with no interactive product (use image-design).
---

# Software Design

Before starting, read `../design-core/SKILL.md` (shared process, depth modes) and use `../design-core/references/templates.md`. If those files aren't available, follow: brief → users → design DNA → 3 concepts → critique → prototype → real-render review → handoff. This skill adds what is specific to interactive digital products.

## Artifacts (scale to depth)

brief · user panel · task/journey map · reference scan · design DNA · information architecture · 3+ concept directions · key flow wireframe · visual system · prototype or implementation · real-render review · accessibility/responsive/performance checks · handoff.

Rapid depth: brief, DNA, IA sketch, one built flow, real-render review, handoff.

## Users

For each primary group capture: top task, frequency, context/device, expertise, information priority, error cost, trust requirements, accessibility needs. Design for behaviour and comprehension first — an expert dispatcher and a first-time banking user need opposite densities, and both are "good UX".

## Information architecture before styling

Define objects/content, grouping, navigation, primary vs secondary actions, and **every state**: empty, loading, error, partial, success, offline where relevant. Missing states are the most common reason a beautiful mock becomes a frustrating product.

## Concepts = different interaction models

Vary the model, not the theme: progressive vs dense · guided vs expert · spatial vs linear · conversational vs direct manipulation · dashboard vs task-first · content-first vs tool-first. Wireframe-level is enough to compare.

## Visual system

Define spacing rhythm (e.g. 4/8-pt), grid, type scale and hierarchy, colour **roles** (not just swatches: surface, text, accent, success/warn/error, focus), elevation logic, icon and image language, controls, states, motion principles. Express them as tokens when code is involved so the system survives implementation.

**Avoid the generic AI look** unless the DNA asks for it: purple-blue gradients on dark, glassmorphism cards everywhere, emoji as icons, centred hero + three feature cards by default, vague "Unlock the power of…" copy. These read as unconsidered because they are the path of least resistance.

## Implementation

1. Inspect the existing stack and conventions before adding dependencies.
2. Build the highest-value flow first, end to end, before secondary pages.
3. Use semantic HTML / native platform controls — they bring keyboard, screen-reader, and form behaviour for free.
4. Make responsive behaviour intentional (what reflows, what hides, what changes priority), not just "it shrinks".
5. Avoid inaccessible traps: hover-only content, focus traps, click handlers on non-interactive elements, placeholder-as-label.
6. Don't add decorative complexity that harms performance.

## Motion

Use motion to explain hierarchy, causality, state change, spatial relationships, and continuity. Typical UI durations: 100–200 ms for micro-feedback, 200–400 ms for larger transitions. Always honour `prefers-reduced-motion`. See motion-pictures for full motion languages.

## Real-render review

Render and look — screenshots at roughly 375, 768, and 1440 px wide, or the target device sizes. If you can't render in this environment, say so and give the user the exact checklist below.

Concrete checks (WCAG 2.2 AA as the floor):
- Text contrast ≥ 4.5:1 (≥ 3:1 for large text: 24 px, or ~19 px bold); UI components and focus indicators ≥ 3:1
- Pointer targets ≥ 24×24 CSS px minimum; aim for 44×44 on touch
- Visible focus that isn't hidden by sticky headers; full keyboard path through the key flow
- Reflows without horizontal scroll at 320 CSS px; usable at 200% text zoom
- Text measure ~45–80 characters for reading copy
- All states from IA present and designed
- Performance targets for web: LCP ≤ 2.5 s, INP ≤ 200 ms, CLS ≤ 0.1
- First-glance comprehension: in 5 seconds, can a target user say what this is and what to do?

## Handoff

Include: the implemented/prototyped experience, rationale with traceability, component and token notes, responsive rules, accessibility notes (what was checked and how), unresolved risks, and one recommended usability test (task, participant profile, success measure).
