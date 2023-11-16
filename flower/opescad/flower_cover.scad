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

module draw_flower(height, radius) {
    draw_line_extra(-1,2, 3, height, radius);
    draw_line_extra(0,1, 7, height, radius);
    draw_line_extra(1,1,2, height, radius);

    draw_line_extra(1,4, 4, height, radius);
    draw_line_extra(2,4, 4, height, radius);
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
        draw_flower(30, br+0.8+1);

        translate([-1,0,0]) draw_flower(29, br+0.8);
        
        translate([28-10,0,-15/2]) cube([10,50,15]);        
        translate([31-10,0,-7/2]) cube([7,1000,7]);        

    }
}
