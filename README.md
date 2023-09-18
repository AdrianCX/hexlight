Simple 3D Printed hex night light.

![Alt text](/pictures/overview.jpg "")


1. Components used:

1.1. Raspberry pi pico
- https://www.tinytronics.nl/shop/en/development-boards/microcontroller-boards/with-wi-fi/raspberry-pi-pico-w-rp2040

1.2. WS2813 LED strip 30 per meter:
- https://www.tinytronics.nl/shop/en/lighting/led-strips/led-strips/worldsemi-ws2813-digital-5050-rgbw-led-strip-30-leds-5m

1.3. Random perf board / button and plastic housing for pico

This is mostly to make life easier and not have a lot of cables running through.

2. 3D printed parts:

Files are in openscad/ folder.

Important settings for printer:
- top/bottom pattern - concentric
- comb mode (they're pretty thin pieces, should print without any retractions or jumps)

2.1. You can print each hex individually:
- single_hex.scad (.stl for cura)
- 3_hex_holder.scad (.stl for cura)
- support.scad (.stl for cura)

You will need a lot of pieces and some glue to fix things to the support pieces (which also need to be glued together or on some support)

2.2. OR you can print out the full hex board (change the scad file to make it fit your 3d printer)
- fullhexboard.scad (.stl for cura)
- support.scad (.stl for cura)
- 3_hex_holder.scad (stl for cura) - only need a few pieces to merge the full boards together.


3. Building it:

![Alt text](/pictures/building.jpg "")

Cut the led strips into 5 or more rows and arrange as above.
Should be easy to do with more or less rows / columns, just change scad files as needed.


4. Software:

This is in pico folder, runs on micropython.

4.1. main.py
- function Display.__init has 5 rows for leds configured in self.grid, adjust as needed with pins.
- has a few useful functions - one for gradient, one for random rainbows and one for numbers if you want to make a clock

