sx=6.8;

module draw_holder() {
    translate([-9/2,-9/2,0]) cube([9,9,1]);        
    translate([-sx/2,-sx/2, 1]) cube([sx,sx,4]);
    translate([-sx/2,-sx/2, 5]) cube([sx,1,4]);
}

difference() {
    draw_holder();
    translate([-sx/2,-4/2,0]) cube([sx,4, 4]);
    translate([-sx/2,-1,0]) cube([1,2, 10]);
    translate([sx/2-1,-1,0]) cube([1,2, 10]);
}
