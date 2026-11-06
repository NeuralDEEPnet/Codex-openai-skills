# Eval results

## v0.3 — lean-unbranded-landing — 2026-11-05

The skill bodies are shared with the Claude edition, where the case was run with `claude plugin eval` on Claude Sonnet 5.5 (with/without ablation, 3 runs per arm, 3 judge votes per assertion). Directional only.

| Arm | Run 1 | Run 2 | Run 3 | Mean |
|---|---|---|---|---|
| with skills | 5/9 | 4/9 | **8/9** | 0.63 |
| without | 3/9 | 3/9 | 4/9 | 0.37 |

Runs 1–2 ran before the Rapid response shape was added to the house style and dropped the depth line, the anti-principles and the contrast numbers; run 3 ran with the final text and missed only the word-count assertion (a 359-word response that two judges over-counted). The baseline never stated a depth, never listed anti-principles, and gave no contrast numbers. **Clean rerun on the final text** (same setup, 6 runs):

| Arm | Run 1 | Run 2 | Run 3 | Mean |
|---|---|---|---|---|
| with skills | 7/9 | 5/9 | 7/9 | 0.70 |
| without | 3/9 | 3/9 | 3/9 | 0.33 |

Δ +0.37. Runs 1 and 3 followed the Rapid response shape exactly (depth line, artifact, DNA with anti-principles, contrast numbers, honest render statement) at 349 and 350 words, yet all three judges failed the "under 400 words" assertion both times; the judges cannot count reliably, so that grader is now a qualitative compactness check (`07-response-is-compact`). Run 2 did not state the depth, the DNA or the contrast numbers, which looks like the skill not being read on that run; treat 1-in-3 as the current trigger variance on Sonnet. The baseline was stable at 3/9: one file, one accent, short response, and none of the design discipline.

No Codex-native run has been made.

## v0.2 vs v0.1 — 2026-10-28

Executor: Claude Sonnet subagents, one run per configuration. Grader: Claude Opus, assertions in `evals/cases/`. Directional only.

| Case | v0.2 | v0.1 |
|---|---|---|
| vague-premium-brief (design-core) | 6/6 | 4/6 |
| printable-desk-robot (3d-object-design) | 7/7 | 5/7 |
| rapid-404-page (software-design) | 7/7 | 5/7 |
| **Pass rate** | **100%** | **70%** |
| Avg tokens / time | 95k / 47 s | 90k / 43 s |

**What actually changed in behaviour**
- Specialist runs now produce a hypothesis user panel and DNA with anti-principles (v0.1's 3D run skipped both because the specialist skill never pointed to design-core).
- Quick requests stay quick but keep a compact DNA; the 404 run also caught that the server must return a real 404 status.
- Clarifying questions capped at 3 with stated assumptions (v0.1 asked 6).

**Caveats**
- Several assertions encode rules introduced in v0.2, so part of the gain is the new skill graded against its own rules. Checks that both versions passed (style restraint, numeric FDM rules, contrast, reduced motion) show v0.1 was already strong on Sonnet.
- The vague-brief answer grew ~25% (2,033 vs 1,638 words). Watch length on open-ended briefs.
