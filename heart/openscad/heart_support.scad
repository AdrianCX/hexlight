$fn=200;

// radius for hex
br=18.8;
// height for hex
bh=0.8;

// Distance between 2 hexes
dist=33;


board();

module draw_line(j, start, end) {
    for ( i = [start : end] ){
        translate([0,i*dist+(dist/2*(j%2)),j*28.6]) rotate([0,90,0]) cylinder(r=br+0.4,h=bh, $fn=6);
    }
}


module board() {
    difference() {
        translate([0,0,0]) {
            draw_line(0,2, 5);
            draw_line(1,1,5);
            draw_line(2,1,6);
            draw_line(3,1,6);
            draw_line(4,4,6);
            draw_line(5,4,5);
        }
    }
}
