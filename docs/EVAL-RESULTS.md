# Eval results

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
