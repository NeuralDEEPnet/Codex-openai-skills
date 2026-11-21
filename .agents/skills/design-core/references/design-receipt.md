# Design Receipt

A Design Receipt is the evidence that ships with every deliverable: what was made, what was measured, what each decision traces to, what was *not* checked, and how AI was used. It is the studio's answer to "prove it" from a client, a reviewer, or a regulator, and it is what turns an attractive output into a defensible one.

Receipts are mandatory at every depth. A Rapid receipt is a dozen lines; a Full receipt is a document. The content is the same shape so receipts are comparable across projects and media.

Specification: **Neuraldeep Design Receipt v1** (2026-11). It extends the 3DJ Design Evidence Pack v1, whose confidence labels and manufacturing gates it reuses for physical parts.

## Rules

1. **Numbers, not adjectives.** "Readable" is a claim; "15.3:1 body text on paper, 6.1:1 primary action, both themes" is a receipt. Every check that can be measured is measured, and the method is named.
2. **The not-done list is mandatory.** What was not rendered, measured, tested, or known is listed, in one line each. An empty not-done list is a defect, because nothing is ever fully verified.
3. **Every fact carries its confidence.** Use one of: `measured` (instrument, formula, kernel, or test), `observed` (seen on a real render, print, playback, or device), `inferred` (reasoned from conventions or references), `assumed` (unverified; awaiting confirmation). Never upgrade a label to make the receipt look stronger.
4. **Every important decision traces to something.** A user need, a constraint, or a DNA principle. A decision that traces to nothing is taste; say so.
5. **Research keeps its tags.** `[evidence] [opinion] [trend] [inspiration] [inference]` from design-core carry through into the receipt, with sources and dates. No invented users, quotes, analytics, or test results, ever.
6. **AI use is disclosed per artifact**, in plain words: which steps were AI-generated, AI-assisted, or human-made; which models or tools; what a person reviewed. This is a factual statement for the client's own disclosure duties, not a legal opinion.
7. **Say what would change the verdict.** One line: the evidence that would overturn the main decision.

## The receipt

Use this layout. Delete rows that genuinely do not apply; keep "Not done" and "AI use" always.

```markdown
## Design Receipt — <artifact name> — <date>
**Spec:** Neuraldeep Design Receipt v1 · **Depth:** Rapid | Standard | Full · **Medium:** software | image | 3D object | motion | virtual world | multi

### Artifact
| Item | Value |
|---|---|
| Files | <paths, versions, formats, colour space / units> |
| Built with | <tools, versions, scripts, models> |
| Brief | <one line> · **DNA:** <three principles, two anti-principles> |

### Decisions
| Decision | Traces to | Confidence |
|---|---|---|
| <what was decided> | <user need / constraint / DNA principle> | measured · observed · inferred · assumed |

### Checks
| Check | Method | Result | Threshold | Pass |
|---|---|---|---|---|
| <e.g. body text contrast, light> | WCAG 2.x formula | 15.3:1 | ≥ 4.5:1 | yes |

### Not done
- <what was not rendered / measured / tested, and what the user should do instead>

### Research
| Finding | Tag | Source (date) | Used for |
|---|---|---|---|

### AI use
| Step | How made | Tools / models | Reviewed by |
|---|---|---|---|
| <e.g. hero image> | AI-generated | <model> | <person / agent> |

### Risks and next step
- **Unresolved:** <risk, who owns it>
- **Would change our mind:** <the evidence>
- **Next validation:** <one test: who, what, success measure>
```

A machine-readable twin (`receipt.json`) uses the same section names as keys; keep both when a client or pipeline will ingest it.

## Checks by medium

Starting points. Thresholds come from the specialist skills; a receipt may add checks, never silently drop these.

**Software**
- Text contrast per role per theme (WCAG 2.x formula); UI component and focus contrast ≥ 3:1
- Pointer targets (≥ 24 × 24 CSS px; 44 × 44 on touch)
- Keyboard path through the key flow; visible focus
- Reflow at 320 CSS px; 200 % zoom
- States present: empty, loading, error, success
- `prefers-reduced-motion` honoured
- Widths rendered (e.g. 375 / 768 / 1440) and *which were not*
- Web performance when measurable: LCP, INP, CLS
- Dependencies and licences

**Image**
- Final sizes and ratios delivered; crop test at smallest use
- Text-safe areas respected (measure, not eyeball)
- Generation artefacts inspected (hands, text, geometry, duplicated features, logos)
- Trademark, likeness, and reference use stated
- Colour space and bit depth

**3D object** (reuse the 3DJ Design Evidence Pack v1 gates)
- Watertight: 0 open edges, 0 non-manifold edges; kernel named
- Bounding box, volume, mass by material, centre of mass
- Minimum wall vs process (FDM: 0.8 mm nozzle-safe, 1.2 mm recommended); overhangs vs 45°
- Build envelope fit (e.g. 220 × 220 × 250 mm) with orientation
- Assembly: interference volume (0.00 mm³ gate), minimum clearance, joint sweeps
- Dimension confidence: measured ± 0.15 mm · observed ± 0.35 mm · inferred ± 0.80 mm · assumed
- Export format and provenance (ISO 10303-21 STEP, binary STL, GLB)
- Fit coupon printed? Physical test? If not, say so

**Motion**
- Duration per beat sums to target length
- No flashing > 3 per second (WCAG 2.3.1)
- Reads with sound off; captions present
- Reduced-motion alternative exists and was viewed
- Played at real speed on target device? Which crops (16:9, 1:1, 9:16) were checked?

**Virtual world**
- Frame time against platform budget (e.g. 72–90 Hz → 11–14 ms), measured where and how
- Draw calls, triangles, texture memory vs budget
- Locomotion and comfort options present; text distance and lock mode
- Safety and moderation controls for social spaces
- Tested on target device at intended scale? With first-time users?

## Depth scaling

| Depth | Receipt |
|---|---|
| Rapid | Artifact, three to five decisions, the checks that were run with numbers, Not done, AI use, one next step. Fits in the chat response. |
| Standard | Every section, tables short. |
| Full | Every section, with the research log and a validation plan; `receipt.json` alongside. |

## Receipts for work you did not make

When reviewing someone else's artifact (see the `design-review` skill), the receipt records what you could verify about it: the checks you ran, the ones you could not, and the decisions you could and could not trace. Say whose artifact it is and that the receipt is a review, not an authorship claim.

## What a receipt is not

Not a certification, not a legal opinion, not proof of fitness for purpose. Geometry gates are diagnostics; print readiness needs slicer inspection and a physical part. Accessibility numbers show conformance on the measured items, not a full audit. The receipt says exactly this in its own words where a client might otherwise over-read it.
