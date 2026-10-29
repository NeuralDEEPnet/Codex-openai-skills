// Neural Deep Network Ltd / 3DJ — Parametric acoustic RELIEF tile, v0.1
// 3D-printable *decorative* face. Actual acoustic absorption requires a measured
// porous backing and acoustic testing; PETG surface alone is not an absorber.
// Units: millimetres. Suggested print orientation: rear face flat on bed.
// Fully self-contained OpenSCAD; change parameters and press F6 then export STL.

panel_width = 160;             // MINI+ usable bed is nominally 180x180 mm
contour_count = 6;             // six concentric surface crests
relief_height = 19;           // highest crest over the 5mm nominal backing
back_thickness = 5;
mount_count = 4;              // four independent rotational mounting directions
mount_offset = 52;            // radial centre of each keyhole entry
mount_travel = 11;            // head slides toward nearest edge
mount_head_radius = 4.2;      // fits a head up to nominal 8.4 mm diameter
mount_neck_radius = 2.25;     // accepts nominal 4 mm shaft (allowance ~0.5 mm)
mount_pocket_depth = 3.6;     // concealed head cavity from back plane
mount_lip_thickness = 1.3;    // rear lip retains screw head in narrow slot
radial_steps = 40;            // decrease for fast previews; >= 30 for final
angular_steps = 72;           // must be divisible by 4
squircle_power = 6;           // 2=circle, >2=rounded square

assert(panel_width > 0 && panel_width <= 180);
assert(contour_count >= 1 && contour_count <= 12);
assert(relief_height > 0 && back_thickness > mount_pocket_depth+1.0);
assert(mount_count == 4 && angular_steps % 4 == 0);

// By design, the outer boundary (r=1) and centre (r=0) meet nominal backing.
function sign0(x) = x < 0 ? -1 : 1;
function sqcos(t) = sign0(cos(t)) * pow(abs(cos(t)), 2/squircle_power);
function sqsin(t) = sign0(sin(t)) * pow(abs(sin(t)), 2/squircle_power);
function ridge_at(r,k) =
    (0.55 + 0.45*sin(180*(k+0.5)/contour_count))
    * exp(-pow((r-(0.125 + k*0.75/max(1,contour_count-1)))/0.056,2));
function raw_ridge(r) = max([for(k=[0:contour_count-1]) ridge_at(r,k)]);
function top_z(r) = back_thickness + relief_height*raw_ridge(r)/raw_ridge(0.575);

// Top radial rings (1..steps), plus single centre, lower perimeter and lower centre.
function ring_vertex(i,j) =
    let(r = i / radial_steps, a = 360*j/angular_steps)
    [panel_width/2*r*sqcos(a), panel_width/2*r*sqsin(a), top_z(r)];
function bottom_vertex(j) =
    let(a = 360*j/angular_steps)
    [panel_width/2*sqcos(a), panel_width/2*sqsin(a), 0];
function topid(i,j) = 1+(i-1)*angular_steps+(j%angular_steps);
function botid(j) = 1+radial_steps*angular_steps+(j%angular_steps);
function botcenter() = 1+(radial_steps+1)*angular_steps;

module parametric_tile_blank() {
    points = concat(
        [[0,0,top_z(0)]],
        [for(i=[1:radial_steps],j=[0:angular_steps-1]) ring_vertex(i,j)],
        [for(j=[0:angular_steps-1]) bottom_vertex(j)],
        [[0,0,0]]
    );
    faces = concat(
        // Top centre fan (CCW)
        [for(j=[0:angular_steps-1]) [0,topid(1,j),topid(1,j+1)]],
        // Top: two triangles per quad
        [for(i=[1:radial_steps-1], j=[0:angular_steps-1])
            each [[topid(i,j),topid(i+1,j),topid(i+1,j+1)],
                  [topid(i,j),topid(i+1,j+1),topid(i,j+1)]]],
        // Outer vertical wall
        [for(j=[0:angular_steps-1])
            each [[topid(radial_steps,j),botid(j),botid(j+1)],
                  [topid(radial_steps,j),botid(j+1),topid(radial_steps,j+1)]]],
        // Back face (CW when viewed from top)
        [for(j=[0:angular_steps-1]) [botcenter(),botid(j+1),botid(j)]]
    );
    polyhedron(points=points,faces=faces,convexity=15);
}

module single_keyhole() {
    // At this local +Y axis, the large opening receives the screw head.
    // Sliding toward +Y captures the head under a 1.3 mm retaining lip.
    // OPENINGS ON BACK, not on the visible sculpted front.
    translate([0,mount_offset,0]) {
        // Entry opening for the screw head
        translate([0,0,-0.15]) cylinder(r=mount_head_radius,h=mount_pocket_depth+0.3,$fn=40);
        // Narrow shaft path accessible from rear face
        hull() {
            translate([0,0,-0.15]) cylinder(r=mount_neck_radius,h=mount_lip_thickness+0.20,$fn=24);
            translate([0,mount_travel,-0.15]) cylinder(r=mount_neck_radius,h=mount_lip_thickness+0.20,$fn=24);
        }
        // Enlarged undercut cavity behind the lip so the head can travel
        hull() {
            translate([0,0,mount_lip_thickness]) cylinder(r=mount_head_radius,h=mount_pocket_depth-mount_lip_thickness,$fn=40);
            translate([0,mount_travel,mount_lip_thickness]) cylinder(r=mount_head_radius,h=mount_pocket_depth-mount_lip_thickness,$fn=40);
        }
    }
}

difference() {
    parametric_tile_blank();
    for (a=[0:90:270]) rotate([0,0,a]) single_keyhole();
}
