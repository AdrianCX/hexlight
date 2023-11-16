Flower shaped hexagon light

![Alt text](/flower/pictures/1.jpg "")

Software is in pico subfolder.
CAD/STL files for 3D printed files are in openscad subfolders.

Parts are:
- Raspberry pi pico
- Button: https://www.kiwi-electronics.com/nl/drukknop-6mm-slim-20-stuks-606?search=button
- 1000uF capacitor
- WS2813 led strip
- M2/M3 standoffs and screws.


Soldering done is visibile in pictures:
- 1000uF capacitor between VBUS/GND
- Button on GPIO
- Connected data pin to pico on GPIO 0

How to assemble and make

1. End result before assembly

![Alt text](/flower/pictures/2.jpg "")

Holes are drilled with M2/M3 bits and using standoffs to fix in place.

A small button is fixed on the bottom with the button_holder.scad piece.

Otherwise you can use any smaller/larger buttons as needed, hole should be 7x7mm (but in practice usually is 6.8/6.8)

2. Leds attached to holder:

![Alt text](/flower/pictures/3.jpg "")

![Alt text](/flower/pictures/4.jpg "")

Just cut the led strip as needed and place it through holes on the holder.
Make sure to drill holes before attaching leds.

3. Bottom part

![Alt text](/flower/pictures/5.jpg "")

This is just a regular cover to hide away the cables and microcontroller, drill and attach standoffs for the pico.

