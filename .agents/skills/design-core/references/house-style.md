# House style — lean and clean

Neuraldeep's own way of working and, when nothing else is specified, its default visual character. Two layers, with different scope:

| Layer | Applies | Overridable |
|---|---|---|
| **Lean delivery** — how the studio works and talks | Always, in every medium and depth | No |
| **Clean default character** — a visual baseline | Only when the brief has no brand, design system, or stated style, or the user asks for "the Neuraldeep look" | Yes — the project's own design DNA always wins |

The repository stays style-agnostic: a client brief with its own identity never inherits the clean character. It always inherits lean delivery.

## Where this comes from

- **[evidence]** neuraldeep.net (observed 2026-11-05): near-black ink `#171A1C` on warm off-white paper `#F4EFE6`; Avenir 85 Heavy headings with Helvetica Light body; a four-word headline ("AI design agents. Ideas into reality."); one call to action per view; pale sky `#BDE9FB`, blush `#EAE0DA` and sage `#D0E0CD` as occasional surface tints.
- **[opinion]** The owner describes the intended philosophy as "lean and clean, fresh".
- **[inference]** Everything below that turns those observations into rules. Treat it as the studio's working interpretation, not as a published brand manual.

## Lean delivery (always)

1. **Answer first.** The artifact or the decision leads; rationale follows and stays proportionate to the depth chosen (see the budgets below).
2. **Artifacts, not essays.** Use the templates. Fill rows that matter, delete rows that don't. No "N/A" padding.
3. **One next step.** Every handoff ends with the single most useful validation, not a list of everything one could do.
4. **No filler.** No restating the brief back, no throat-clearing, no "in today's fast-paced world". Each sentence either decides, shows, or warns.
5. **State the gaps plainly.** What was not rendered, measured, tested, or known is said in one line, not buried.
6. **Subtract before you add.** When a design or a document feels weak, remove something before adding something. Add one thing back only if removal broke it.
7. **Targeted revisions stay targeted.** A change to an approved design reuses its brief and DNA. Implement, inspect, hand off. Don't restart research.

### Output budgets

Rough ceilings for the chat response that accompanies a delivered artifact. The artifact itself (page, image, model, film, world) can be as large as it needs to be.

| Depth | Chat response | Process artifacts |
|---|---|---|
| Rapid | ≤ 400 words | brief (3–5 lines), compact DNA, real-output check, handoff |
| Standard | ≤ 1,200 words plus tables | every stage, each table short |
| Full | as needed, sectioned | every stage in depth, each section skimmable in a minute |

If the response blows the budget, that is a signal to move detail into the artifact or a reference file, not to cut the checks.

## Clean default character (only when unbranded)

### Principles — each one can reject a design

1. **One ink, one paper, one accent.** Text colour, background colour, and a single interactive colour. Status colours (success, warning, error) exist but never decorate.
2. **Whitespace is the structure.** Grouping and hierarchy come from spacing on one scale before they come from lines, boxes, or shadows. Rejects: a page where every group has a card border.
3. **Two type weights, one family.** A heavy display weight and a light-to-regular text weight. Size and weight carry hierarchy; colour does not. Rejects: three fonts, or body copy in four greys.
4. **Say it in one line.** Headlines are declarative fragments. Buttons are verbs. Copy names real things (a machine, a material, a place) over adjectives. Rejects: "Unlock the power of…".
5. **Honest surfaces.** No gradients, glass, blur, or glow that don't carry information. Photography and renders show the real product, process, or material, not stock metaphors.
6. **Fresh means current and quiet, not novel.** Modern defaults (system fonts, dark theme, fluid layout, reduced motion) applied without spectacle. Rejects: the generic AI look (purple-blue gradient on dark, glass cards, emoji icons, centred hero + three feature cards).
7. **Motion explains, then gets out of the way.** 150–250 ms, ease-out, only on state change. Nothing loops.

### Anti-principles — it must not become

- sterile: whitespace with nothing worth looking at
- template-like: the same hero/three-cards/testimonial stack as everyone else
- luxury pastiche: serif + gold + black as a substitute for substance
- minimal-but-hard: hidden navigation, unlabelled icons, grey-on-grey text that fails contrast

### Starter tokens

Derived from the observed site colours; the accent and dark-theme values are derived, not observed. Contrast ratios computed with the WCAG 2.x formula.

```css
:root {
  --paper: #F4EFE6;   /* background */
  --ink:   #171A1C;   /* text — 15.3:1 on paper */
  --ink-2: #4E4F4F;   /* secondary text — 7.2:1 */
  --rule:  #BDBAB4;   /* hairlines, dividers — not for text */
  --accent: #16607D;  /* links, primary action — 6.1:1 on paper; derived from the site's pale sky */
  --accent-wash: #BDE9FB; /* tinted surface only, never text */
  --ok: #1E7A4A; --warn: #8F4E08; --error: #B42318; /* ≥ 4.6:1 on paper */
  --space: 8px;       /* spacing scale: 1, 2, 3, 4, 6, 8, 12, 16 × --space */
  --radius: 4px;      /* one radius; 0 is also fine */
  --font-display: "Avenir Next", "Avenir", "Inter", system-ui, sans-serif; /* weight 700–800 */
  --font-text: "Helvetica Neue", Helvetica, Arial, system-ui, sans-serif;  /* weight 300–400 */
  --measure: 65ch;
  --ease: cubic-bezier(.2,.7,.2,1); --dur: 180ms;
}
:root[data-theme="dark"] {
  --paper: #171A1C; --ink: #F4EFE6; --ink-2: #BDBAB4; /* 9.0:1 */
  --rule: #4E4F4F; --accent: #7FCBEA; /* 9.7:1 on dark paper */
  color-scheme: dark;
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --paper: #171A1C; --ink: #F4EFE6; --ink-2: #BDBAB4;
    --rule: #4E4F4F; --accent: #7FCBEA;
    color-scheme: dark;
  }
}
```

Type scale: 14 / 16 / 20 / 28 / 40 / 56 px, line-height 1.4 for text and 1.1 for display. The site's largest heading is 56–60 px.

### Grey text

`#868581` (the site's mid grey) is 3.2:1 on paper: large text only (≥ 24 px, or 19 px bold), never body copy. On dark paper it is 4.7:1 and passes for body text.

## The reduction pass

Run once before handoff in every medium, at every depth. Each line is a yes/no check; a "no" is a defect, not a style preference.

**Any medium**
- Could a first-time viewer say what this is and what to do within 5 seconds?
- Is there one clear focal point, and does everything else rank below it?
- Does every element carry information, structure, or affordance? List what carries none and remove it.
- Are there more than three of anything where one would do (colours, fonts, radii, shadow styles, icon styles, animation curves)?

**Software**
- One accent colour, one spacing scale, one radius, one elevation logic.
- Every border or shadow: would spacing alone do the job?
- Copy: every heading a fragment, every button a verb, no sentence over ~20 words.
- States present: empty, loading, error, success. Reduced-motion honoured.

**Image**
- One subject, one message, one light. Negative space does the framing.
- Crop test: does the read survive at 150 px and at 9:16?

**3D object**
- Silhouette reads in pure black. Radii belong to one family. Part lines only where assembly or tolerance needs them.
- Surface detail that does not serve grip, ventilation, assembly, or wear is removed.

**Motion**
- Every beat changes what the viewer understands. Dead time cut.
- One easing family. Nothing loops without purpose. Reads with sound off.

**Virtual world**
- Orientation from landmarks and light, not from floating UI.
- Every object either affords, informs, or frames. Remove the rest and recover frame time.

## Applying it

- **Unbranded brief** ("a landing page for my tool", "a case for this board"): adopt the clean character as the starting DNA, say so in one line, and still write the project's own anti-principles.
- **Branded brief**: use the client's identity. Lean delivery and the reduction pass still apply.
- **"Make it Neuraldeep"**: use the starter tokens and principles above and the observed site evidence; do not invent further brand rules and say that the tokens are a working derivation.
