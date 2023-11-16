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

hs=11;

module draw_flower() {
    draw_line(-1,2, 3);
    draw_line(0,1, 7);
    draw_line(1,1,2);

    draw_line(1,4, 4);
    draw_line(2,4, 4);
}

module draw_flower_holes() {
    draw_hole_left(1,4, 4);
    draw_hole_right(1,4, 4);
    draw_hole_left(2,4, 4);
    draw_hole_right(2,4, 4);
    draw_hole_left(-1,3, 3);
    draw_hole_right(-1,2, 2);
    
    draw_hole_right(1,1,1);
    draw_hole_left(1,2,2);
    draw_hole_right(0,1, 1);

    draw_hole_left(0,7, 7);

}

module draw_hole_left(j, start, end) {
    for ( i = [start : end] ){
            translate([-15,i*dist+(dist/2*(j%2))+8,j*28.6+hs/2]) rotate([0,90,0]) {
                cube([hs,3,30]);
            }
        }
    }
    
module draw_hole_right(j, start, end) {
    for ( i = [start : end] ){
            translate([-15,i*dist+(dist/2*(j%2))-8-3,j*28.6+hs/2]) rotate([0,90,0]) {
                cube([hs,3,30]);
            }
    }
}

module draw_line(j, start, end) {
    for ( i = [start : end] ){
        translate([0,i*dist+(dist/2*(j%2)),j*28.6]) rotate([0,90,0]) {
            cylinder(r=br+0.4,h=bhh, $fn=6);
            
            rotate([180,0,0]) difference() {
                cylinder(r=br-0.6,h=bh, $fn=6);
                translate([-offx/2,-offy/2,0]) cube([offx,offy,bh]);
                translate([-7.5,-33,0]) cube([15,100,bh]);
                
            }
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
        draw_flower();
        draw_flower_holes();
        
    }
}
