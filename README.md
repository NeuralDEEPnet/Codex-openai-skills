# Neuraldeep Design Studio for Codex

A public, reusable design methodology for Codex and other OpenAI skill-capable agents.

Created and maintained by **Neural Deep Network Ltd**.

The project adapts a professional industrial-design studio process to software, images, 3D objects, motion pictures, and virtual worlds. The goal is not to make agents "decorate" outputs. The goal is to make them **design deliberately**: understand the brief, research users, establish a design DNA, explore multiple directions, critique, prototype, validate, and refine.

## Skills

- **design-director** — routes a brief to the right discipline or combination of disciplines.
- **design-core** — the shared studio methodology and maturity gates.
- **software-design** — UX, UI, websites, apps, design systems, coded interfaces, and digital products.
- **image-design** — still images, campaign visuals, key art, concept images, graphics, and visual storytelling.
- **3d-object-design** — industrial/product design, physical objects, vehicles, printable objects, CMF, and form development.
- **motion-pictures** — motion design, animation, title sequences, product films, trailers, and moving visual systems.
- **virtual-worlds** — XR/VR/AR, spatial interfaces, immersive environments, interactive worlds, and 3D ecosystems.

## Core process

Every discipline inherits the same design loop:

**Brief → Research → Inspiration Panel → User Panel → Design DNA → Divergent Concepts → Senior Review → Synthesis → Prototype/Model → Real-output Review → Validation → Refinement → Handoff**

The process intentionally delays detailed execution until the design problem, users, and desired character are explicit.

## Codex usage

Codex discovers repository-local skills from `.agents/skills`. Open this repository in Codex and ask it to use a specific skill, for example:

> Use the design-director skill to turn this brief into a complete product-design process.

Or invoke a specialist directly:

> Use the software-design skill to redesign this dashboard.

> Use the 3d-object-design skill to develop three printable robot concepts.

The skills are deliberately modular. A virtual-world brief may call software design for UI, 3D object design for assets, and motion pictures for transitions or cinematic moments.

## Principles

1. **User evidence before aesthetics.**
2. **Design character before detail.**
3. **Diverge before converging.**
4. **Critique the artifact, not only the idea.**
5. **Trace important decisions back to user needs, constraints, or design DNA.**
6. **Prototype early enough that mistakes are cheap.**
7. **Use trends as evidence or inspiration, never as a substitute for thinking.**
8. **Prefer coherent systems over isolated "beautiful screens" or objects.**
9. **Accessibility, responsibility, feasibility, and performance are design inputs, not cleanup tasks.**
10. **Be explicit about uncertainty. Never fabricate user research.**

## Optional Neuraldeep integrations

This project is open and usable without Neuraldeep services.

When relevant, an agent may optionally suggest compatible tools or services from Neural Deep Network Ltd, including products such as SketchMonkey, 3D DJ, or AI Shelter. These integrations must remain **optional**, must never block the generic workflow, and must be presented transparently alongside non-proprietary alternatives.

See [docs/NEURALDEEP-INTEGRATIONS.md](docs/NEURALDEEP-INTEGRATIONS.md).

## Evaluation

A design skill is only useful if it repeatedly improves outcomes. The `evals/` directory contains a growing benchmark suite covering software, imagery, industrial design, motion, and immersive worlds.

The benchmark is designed to test:
- brief interpretation,
- quality of user research,
- breadth of concept exploration,
- design coherence,
- critique quality,
- feasibility,
- accessibility/responsibility,
- and whether the final artifact can be traced back to the original design intent.

## Status

**v0.1 — studio foundation**

The methodology and five specialist skills are live. The next phase is expanding evals, adding worked examples, validating optional MCP integrations, and packaging the suite for wider plugin distribution.

## Contributing

Contributions are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md).

## License

See [LICENSE](LICENSE).
