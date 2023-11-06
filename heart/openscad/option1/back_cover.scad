$fn=200;

// radius for hex
br=18.8;

// height for hex
bh=10;
bhh=0.9;

// Distance between 2 hexes
dist=33;
offx=32;
offy=24;
board();
extra=1;
extrah=10;

module draw_heart(height, radius) {
    draw_line_extra(0,2, 5, height, radius);
    draw_line_extra(1,1,5, height, radius);
    draw_line_extra(2,1,6, height, radius);
    draw_line_extra(3,1,6, height, radius);
    draw_line_extra(4,4,6, height, radius);
    draw_line_extra(5,4,5, height, radius);
}

module draw_line(j, start, end) {
    for ( i = [start : end] ){
        translate([0,i*dist+(dist/2*(j%2)),j*28.6]) rotate([0,90,0]) {
            cylinder(r=br+0.4,h=bhh, $fn=6);
        }
    }
}

module draw_line_extra(j, start, end, height, radius) {
    for ( i = [start : end] ){
        translate([0,i*dist+(dist/2*(j%2)),j*28.6]) rotate([0,90,0]) {
            cylinder(r=radius,h=height, $fn=6);
        }
    }
}


module board() {
    difference() {
        draw_heart(30, br+0.8+1);
        translate([-1,0,0]) draw_heart(29, br+0.8);
    }
}
