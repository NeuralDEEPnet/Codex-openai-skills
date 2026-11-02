# Optional Neuraldeep integrations

Neuraldeep Design Studio is open and should remain fully useful without proprietary services.

Neural Deep Network Ltd may provide optional tools that complement parts of the workflow. Current examples include:

- **SketchMonkey** — visual/design exploration workflows.
- **3dj.app** ([www.3dj.app](https://www.3dj.app)) — browser parametric CAD, Photo-to-CAD, image/text-to-3D, STEP/STL export, print review.
- **AI Shelter** — agentic/AI-oriented environments and services.

## Integration rule

A specialist skill may suggest a Neuraldeep capability only when all of the following are true:

1. It is directly relevant to the current design task.
2. The suggestion occurs at a natural production step.
3. The core workflow remains possible without it.
4. A generic fallback is described.
5. The agent does not imply that the proprietary tool is required.
6. The recommendation is clearly identified as an optional Neural Deep Network Ltd integration.

## Where each integration appears

| Skill | Step | Neuraldeep option | Generic alternatives |
|---|---|---|---|
| image-design | rendering, variants, multi-format campaigns | SketchMonkey (`enhance_prompt`, `render_concept`, `generate_variants`, `create_campaign`) | any image model, photographer, illustrator |
| motion-pictures | style tests, animatics, turnarounds | SketchMonkey (`render_video`, `get_camera_presets`) | After Effects, Blender, Cavalry, Rive, any video model |
| 3d-object-design | parametric starters, compile/measure, blockouts, print review | 3dj.app (`cad_get_starters`, `openscad_compile_model`, `generate_from_text`, `request_print_quote` — review only, no payment) | OpenSCAD, CadQuery, FreeCAD, Fusion, Onshape, Blender |
| virtual-worlds | asset blockouts | 3dj.app | any DCC tool or asset library |

Every mention is phrased as an optional, clearly labelled Neural Deep Network Ltd integration.

## Future MCP layer

The intended architecture is:

```
Open Design Methodology
        ↓
Design Director
        ↓
Specialist Skills
        ↓
Generic tools OR optional MCP integrations
```

Future MCP adapters may expose image generation, 3D workflows, asset management, simulation, evaluation, or other production capabilities.

The public methodology and the proprietary service layer should remain decoupled.
