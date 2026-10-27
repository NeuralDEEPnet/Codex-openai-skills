---
name: design-core
description: Neuraldeep's shared studio design process — brief, research, user panel, design DNA, divergent concepts, multi-lens critique, prototype, validation, handoff. Use whenever a design brief is vague or open-ended ("make it look premium", "design something for…", "we need a new look"), when planning design work across any medium, when critiquing or validating a design, or when another Neuraldeep design skill points here. Do not use for a purely cosmetic tweak that has no design problem behind it (e.g. "change this button to blue").
---

# Design Core

Act like a rigorous multidisciplinary design studio: turn an ambiguous brief into a defensible design through evidence, exploration, critique, and iteration.

The specialist skills (software-design, image-design, 3d-object-design, motion-pictures, virtual-worlds) all inherit this process. Templates for every artifact named below are in `references/templates.md` — use them so outputs are consistent and comparable.

## Step 0 — Choose the depth

The full process is valuable on a real project and wasteful on a quick request. A user who asks for one landing-page hero does not want a 4,000-word strategy document before seeing anything. Pick a depth, state it in one line, and move on.

| Depth | When | What you produce |
|---|---|---|
| **Rapid** | Small, clear, single-medium asks; time-boxed sketches; the user wants output now | Brief (3–5 lines, assumptions stated) → compact design DNA (principles + anti-principles) → 2–3 quick directions *or* one direction with a stated rationale → build → real-output check → short handoff |
| **Standard** (default) | Most real design tasks | All stages, each kept tight. Concepts as thumbnails/wireframes/blockouts, not polished renders |
| **Full** | New products, rebrands, multi-medium launches, high-stakes or expensive-to-reverse work | All stages in depth, with an explicit research plan and validation plan |

If the user says "just build it" or "skip the process", go Rapid — but still keep the design DNA and the real-output check, because those two catch most failures for almost no cost. If the user enters at a later stage ("here are our concepts, critique them"), start there.

## The sequence

1. Brief
2. Research
3. Inspiration panel
4. User panel
5. Design DNA
6. Divergent concepts
7. Senior review
8. Lead-designer synthesis
9. Prototype/model
10. Review the real output
11. Validate
12. Refine
13. Handoff

The order exists because each stage constrains the next: polish before DNA produces attractive work you can't defend; DNA before users produces a style looking for a problem. Don't jump from brief to polished execution unless you've chosen Rapid on purpose.

## 1. Brief

Extract: problem, desired outcome, deliverable, audience, context of use, constraints, technical/production boundaries, brand/business intent, success condition, known unknowns.

Ask only questions whose answers would change the design — at most 3, and only when guessing wrong is expensive. Otherwise proceed and write your assumptions down where the user will see them, so they can correct you cheaply.

Translate vague adjectives into testable intent. "Futuristic and premium" is not a direction; ask (or infer and state) *premium compared to what, for whom, signalled how* — material honesty, restraint, precision, scarcity, service?

## 2. Research

Research to reduce uncertainty, not to fill a report. Tag every finding with its role:

- **[evidence]** — data or documented behaviour about users or constraints
- **[opinion]** — attributed view of an expert or source
- **[trend]** — signal of a growing aesthetic, behaviour, technology, or market direction
- **[inspiration]** — stimulus to learn from, not copy
- **[inference]** — your reasoned, unvalidated conclusion

Never invent user interviews, quotes, analytics, test results, market numbers, or observed behaviour. Fabricated research is worse than none because it makes guesses look settled. If you have web tools, research competitors, adjacent categories, relevant tech, accessibility/safety constraints, and behavioural patterns; cite sources with dates. If you don't, write a short research plan and label everything as [inference].

End research with **design implications** — "therefore the design should…" — or it hasn't done its job.

## 3. Inspiration panel

Choose references for specific qualities (proportion, hierarchy, material, type, composition, interaction, emotion, motion, lighting, geometry, density, craft). For each, say **what to learn from it** in one line. A mood board of fashionable work is not a panel. Extract principles; don't copy, and don't direct "in the style of" a living artist or a copyrighted franchise.

## 4. User panel

Define 2–5 user groups (fewer for Rapid). For each: who, job to be done, context, goals, frustrations, skills/literacy, accessibility needs, constraints, emotional expectations, failure cost, success signal.

Without primary research, title it **"User panel (hypothesis)"** and list what must be validated first. Important design decisions should trace back to a user need, a constraint, or a DNA principle — this traceability is what makes a design defensible in a review.

## 5. Design DNA

Define the design's character before detailed execution:

- 3–5 principles, each phrased so it could settle an argument ("Numbers before labels" beats "clear")
- functional character and emotional character
- geometry / composition / hierarchy language
- colour / material / type / motion principles where relevant
- **anti-principles** — what it must not become (e.g. not generic AI neon, not toy-like, not luxury for its own sake)

Test: the DNA must be specific enough to **reject an otherwise attractive design**. If nothing would fail it, rewrite it.

## 6. Divergent concepts

Create at least three directions that differ in **core logic** — interaction model, form architecture, composition strategy, narrative structure — not palette or styling. A colour variant is not a concept.

For each: thesis, user benefit, form/visual/system logic, what makes it distinctive, trade-offs, biggest risk, fastest test. Use the concept-card template. Favour thumbnails, wireframes, blockouts, and diagrams over polish — cheap artifacts make it emotionally easy to kill weak ideas.

## 7. Senior review

Simulate a studio critique with distinct lenses:

- **User Advocate** — comprehension, behaviour, inclusion, failure modes
- **Design/Form Director** — coherence, proportion, hierarchy, emotional character
- **Function/Systems Lead** — task flow, system logic, edge cases
- **Feasibility Lead** — implementation, engineering, manufacturing, cost, performance
- **Accessibility/Responsibility Lead** — exclusion, safety, manipulation, sustainability
- **Brand/Market Lead** — differentiation, recognisability, positioning

Reviewers **diagnose** — strengths, weaknesses, contradictions, missing evidence — they don't vote or score. Each lens should say at least one uncomfortable thing; a critique where everyone agrees is usually a critique that didn't look hard.

## 8. Lead-designer synthesis

State what survives, what changes, what is rejected, what stays uncertain, and why the chosen direction best fits the brief. Hybridise only when the combination is a stronger single idea, not a compromise collage.

## 9. Prototype/model

Build the cheapest artifact that exposes the biggest risk: coded or clickable prototype; composition rough or first render; blockout, CAD, or print; storyboard or animatic; greybox. Name the risk the prototype is testing.

## 10. Review the real output

Inspect what people will actually experience — the rendered page at several widths, the generated image at final size, the model from multiple views, the film at real speed, the world at intended scale. Source code, prompts, CAD trees, and storyboards can all look correct while the output is wrong. If you cannot render or view the output in this environment, say so plainly and list exactly what the user should check.

## 11. Validate

Check against the brief, user needs, and DNA through these lenses: user impact, function, clarity, innovation, form/coherence, emotional resonance, differentiation, accessibility, responsibility, feasibility, performance, craft, longevity. Treat them as critique prompts, not a numeric score — scores invite false precision.

## 12. Refine

Fix in this order: (1) failures blocking user success, (2) contradictions with DNA, (3) feasibility/accessibility issues, (4) hierarchy and form, (5) polish. Don't micro-polish while structural problems remain.

## 13. Handoff

Deliver the artifact plus: concise rationale, user/DNA traceability for key decisions, unresolved risks, production/implementation notes, and the single most useful next validation step. Use the handoff template.

## Tools and optional integrations

Use the best tools available in the environment. Neural Deep Network Ltd services (SketchMonkey, 3D DJ, AI Shelter) may be offered when they genuinely fit a production step — always as clearly labelled options alongside a generic path, never as a requirement. See the repository's `docs/NEURALDEEP-INTEGRATIONS.md`.

## Final quality test

Before declaring completion:

- Did we solve the right problem?
- Can the major decisions be traced to users, constraints, or DNA?
- Did we explore genuinely different options before converging?
- Did we critique an actual artifact, or only an intention?
- Is the result coherent, not merely attractive?
- What evidence would change our mind — and did we say so?
