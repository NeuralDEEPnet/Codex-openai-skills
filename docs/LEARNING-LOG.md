# Learning log

## 2026-10-11 — candidate practices
Source: explicit founder corrections across recent design work; no client artifacts copied.
Observation: export fidelity, missing fit measurements, oversized printer parts and archive-only handoffs reduced usefulness.
Scope: physical/print design, with process scaling in design-core.
Rule: inspect exports, verify interfaces and provide visible previews.
Evals: 3d-04, 3d-05, core-03, core-04.
Outcome: structural checks pending; behavioral evaluation pending.
Status: candidate; do not describe as physically validated.

## 2026-11-08 — print path: stale tool knowledge and untriggered skills
Source: repository inspection against the live 3DJ connector catalogue; no client artifacts.
Observation: `capabilities.md` described `cad_validate_script` as syntax-only and the OpenSCAD tools as undeployed, while the live catalogue advertised kernel builds, renders, assembly checks and exports — so an agent following the skill would under-use real tools or misdescribe them. The four print skills had no trigger guidance, no link to the shared process, and no evals.
Scope: create-model, print-production, parametric-printable-surfaces, interactive-3d-print-design.
Rule: a tool reference carries the date it was observed; the skill follows the latest observation and the live description wins at run time. Every skill gets should/shouldn't trigger queries, and the validator fails when one is missing.
Evals: acoustic-tile-honesty, print-01…04, 8 trigger queries.
Outcome: structural checks pass; behavioral evaluation pending.
Status: candidate.

## 2026-11-05 — house style: lean and clean
Source: owner request to embody the neuraldeep.net lean and clean philosophy; site observed directly (colours, type, copy). No client artifacts.
Observation: outputs drifted long (process narration around small asks) and visually generic (second accents, card borders everywhere, template hero stacks) when a brief had no brand.
Scope: all media; design-core and every specialist.
Rule: lean delivery always (answer first, budgets per depth, reduction pass, one next step); clean default character only for unbranded briefs, never overriding a client identity.
Affected: design-core/references/house-style.md, every SKILL.md (reduction pass), software-design (lean defaults, copy).
Evals: lean-unbranded-landing, lean-01…04, trigger queries.
Outcome: structural checks pass; graded case 0.93 with the final text vs 0.37 without over 6 runs each (Claude edition run, Sonnet, directional).
Status: tested.
