$fn=200;

length = 75;
width= 20;
height = 45;

wall=4;

hole_offset_left=33;
hole_offset_height=10;
box_width=2;

// Radius pipe with leds
ir1=16.8/2;
// Height for initial increase
ih1=30;
// Height to keep stable until end of leds
ih2=40;
// Hole radius to be cut later by manual tools
hr1=0.5;

// Position for microcontroller housing
mcr=22.4/2;

// Length for microcontroller hole
mch=60+5;

// Battery radius
br=18.8;
// Battery height
bh=5;

dist=33;
   
translate([-1,26,19]) rotate([0,90,0]) cube(size=[3,14,1]);

difference() {
    translate([0,0,0]) {
        for ( i = [0 : 1] ){
            for ( j = [0 : 1] ){
                translate([0,i*dist+(dist/2*(j%2)),j*28.6]){
                    difference() {
                        translate([-0.4,0,0]) rotate([0,90,0]) cylinder(r=br-0.4,h=bh, $fn=6);
                    }
                }
            }
        }
    }
    translate([-0.4,-100,16]) rotate([0,90,0]) cube(size=[1000,1000,1000]);
    translate([-0.4,-100,1019]) rotate([0,90,0]) cube(size=[1000,1000,1000]);
    translate([-0.4,-974,1000]) rotate([0,90,0]) cube(size=[1000,1000,1000]);
    translate([-0.4,40,1000]) rotate([0,90,0]) cube(size=[1000,1000,1000]);
}
