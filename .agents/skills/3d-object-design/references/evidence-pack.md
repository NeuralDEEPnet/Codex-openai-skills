# Design evidence pack

The standard handoff attachment for any physical or printable design. It replaces "should print fine" with a table a reviewer can audit. One rule governs it: **every value names where it came from**, and the three sources never mix.

| Source tag | Means | Allowed evidence |
|---|---|---|
| **[measured]** | computed from the actual geometry | a CAD-kernel or mesh tool result, a slicer report, a caliper reading — with tool and date |
| **[assumed]** | taken as true without measurement | a datasheet value, a stated default, a user's unverified dimension |
| **[untested]** | a claim nobody has checked yet | fit, strength, heat, acoustic, wear, safety |

Never promote a value: a render does not make a dimension [measured]; a closed mesh does not make a fit tested. If no geometry tool ran, the pack still ships — with the measured rows empty and marked "not run", which is itself the most useful line in it.

## Template

```markdown
### Evidence pack — <part / revision> — <date>
**Geometry source:** <script / file + revision> · **Built with:** <tool, or "not built here">

| Check | Value | Source | Tool / basis |
|---|---|---|---|
| Bounding box (mm) | | [measured] / not run | |
| Volume · mass in <material> | | | |
| Bodies · closed mesh | | | |
| Minimum wall | | | |
| Overhangs > 45° · longest bridge | | | |
| Build-volume fit (<printer>, axis-aligned) | | | |
| Assembly: interference volume · min clearance | | | |
| Joint sweep (range, first collision) | | | |
| Mating interface dimensions | | [assumed] until measured on the real part | |

**Views inspected:** front · top · right · iso · section — or "none; description only"
**Files that exist:** <format + how obtained> · **Files that do not:** <…>
**Untested claims:** <fit / load / heat / acoustic / safety — each with the test that would settle it>
**First physical test:** <the one coupon or print to make first, and what it decides>
```

Delete rows that do not apply (no assembly, no joints). Do not write "N/A".

## Filling it

- **With the 3dj.app connector (optional):** `cad_validate_script` gives bounds, volume, closed-mesh, DfAM and bed fit; `cad_render_views` gives the views (use the `thin-walls` and `overhangs` highlights and a section); `cad_check_assembly` gives interference, clearance and joint sweeps; `cad_export_model` gives the files; `cad_compare_revisions` gives the delta table when a revision changes. Discover the live catalogue first — see `../../create-model/SKILL.md`.
- **Without it:** OpenSCAD or CadQuery for the build, `trimesh` on the exported bytes (`is_watertight`, `body_count`, `volume`, `bounds`), a slicer preview for overhangs and bridges, calipers for interfaces. Same table, same tags.
- **No tool at all:** fill the [assumed] and [untested] rows, mark measured rows "not run", and make "run the build and fill this table" the one next step.

Kernel and mesh measurements are geometry diagnostics. They are not a structural, safety, or manufacturing certification, and the pack must not be presented as one.
