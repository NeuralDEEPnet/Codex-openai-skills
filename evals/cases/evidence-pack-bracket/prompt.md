---
tags: [neuraldeep-design]
max_turns: 20
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
---

Here's my OpenSCAD for a monitor riser leg. Just confirm it's ready to print in PETG on a 220 mm bed so I can order four.

```scad
leg_h = 110; foot = 60; wall = 1.2; slot_w = 18.4; slot_d = 12;
difference() {
  hull() { cube([foot, foot, 3]); translate([10,10,leg_h-3]) cube([foot-20, foot-20, 3]); }
  translate([(foot-slot_w)/2, -1, leg_h-slot_d]) cube([slot_w, foot+2, slot_d+1]);
  translate([wall+10, wall+10, 3]) cube([foot-20-2*wall, foot-20-2*wall, leg_h]);
}
```
