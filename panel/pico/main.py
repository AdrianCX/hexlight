import time

import array, time
from neopixel import Neopixel
from machine import Pin

colors_rgb=[(255, 0, 0, 0),(255, 50, 0, 0),(255, 100, 0,0),(255, 150, 0,0),(255, 200, 0,0),(255, 255, 0,0),
             (0, 255, 0,0), (0, 255, 50,0), (0, 255, 100,0),(0, 255, 150,0), (0, 255, 200,0), (0, 255, 255,0),
             (50, 50, 255,0), (100, 50, 255,0), (150, 50, 255,0),(200, 50, 255,0), (255, 50, 255,0), (255, 100, 255,0),
              (255, 150, 255,0), (255, 200, 255,0),(255, 250, 255,0)]

class Display:
    def __init__(self):
        self.pixels=15
        self.brightness=50
        self.tickupdate=250
        self.deadline = time.ticks_add(time.ticks_ms(), self.tickupdate)

        # Depending on light strip you get you might want to adjust this
        mode="BRGW"
        
        # Pins for each light strip are 16/17/15/19/20 below
        self.grid = [Neopixel(self.pixels, 0, 16, mode),
                     Neopixel(self.pixels, 1, 17, mode),
                     Neopixel(self.pixels, 2, 15, mode),
                     Neopixel(self.pixels, 3, 19, mode),
                     Neopixel(self.pixels, 4, 20, mode)]
        self.clear()
        self.mode="clear"

    def clear(self):
        self.display_type = "clear"

        for i in self.grid:
            i.set_pixel_line(0, self.pixels, (0,0,0,0), how_bright=0)

        self.show()
        
    def show(self):
        for i in self.grid:
            i.show()

    def show_rainbow(self):
        self.deadline = time.ticks_add(time.ticks_ms(), self.tickupdate)

        line=0
        for i in self.grid:
            line=line+1
            for j in range(0,14):
                i.set_pixel(j, colors_rgb[((line*13+j)*time.ticks_ms()*3323)%len(colors_rgb)])
                
        self.show()

    def show_number(self, pos, num, color):
        #RBG
        # 1
        self.grid[0].set_pixel(3*pos, (0,0,0,0))
        self.grid[0].set_pixel(3*pos-1, (0,0,0,0))
        
        self.grid[1].set_pixel(3*pos+1, (0,0,0,0))
        self.grid[1].set_pixel(3*pos, (0,0,0,0))
        self.grid[1].set_pixel(3*pos-1, (0,0,0,0))
        
        self.grid[2].set_pixel(3*pos, (0,0,0,0))
        self.grid[2].set_pixel(3*pos-1, (0,0,0,0))

        self.grid[3].set_pixel(3*pos+1, (0,0,0,0))
        self.grid[3].set_pixel(3*pos, (0,0,0,0))
        self.grid[3].set_pixel(3*pos-1, (0,0,0,0))

        self.grid[4].set_pixel(3*pos+1, (0,0,0,0))
        self.grid[4].set_pixel(3*pos, (0,0,0,0))
        self.grid[4].set_pixel(3*pos-1, (0,0,0,0))

        if num == 0:
            self.grid[0].set_pixel(3*pos, color)
            self.grid[0].set_pixel(3*pos-1, color)
        
            self.grid[1].set_pixel(3*pos+1, color)
            #self.grid[1].set_pixel(3*pos, color)
            self.grid[1].set_pixel(3*pos-1, color)
        
            #self.grid[2].set_pixel(3*pos, color)
            #self.grid[2].set_pixel(3*pos-1, color)

            self.grid[3].set_pixel(3*pos+1, color)
            #self.grid[3].set_pixel(3*pos, color)
            self.grid[3].set_pixel(3*pos-1, color)
            self.grid[4].set_pixel(3*pos+1, color)
            self.grid[4].set_pixel(3*pos, color)
        elif num == 1:
            self.grid[0].set_pixel(3*pos, color)
            #self.grid[0].set_pixel(3*pos-1, color)
        
            #self.grid[1].set_pixel(3*pos+1, color)
            self.grid[1].set_pixel(3*pos, color)
            #self.grid[1].set_pixel(3*pos-1, color)
        
            #self.grid[2].set_pixel(3*pos, color)
            self.grid[2].set_pixel(3*pos-1, color)

            #self.grid[3].set_pixel(3*pos+1, color)
            self.grid[3].set_pixel(3*pos, color)
            #self.grid[3].set_pixel(3*pos-1, color)
            
            #self.grid[4].set_pixel(3*pos+1, color)
            self.grid[4].set_pixel(3*pos, color)
            #self.grid[4].set_pixel(3*pos-1, color)
        elif num == 2:
            self.grid[0].set_pixel(3*pos, color)
            self.grid[0].set_pixel(3*pos-1, color)
        
            self.grid[1].set_pixel(3*pos+1, color)
            #self.grid[1].set_pixel(3*pos, color)
            #self.grid[1].set_pixel(3*pos-1, color)
        
            self.grid[2].set_pixel(3*pos, color)
            self.grid[2].set_pixel(3*pos-1, color)

            #self.grid[3].set_pixel(3*pos+1, color)
            #self.grid[3].set_pixel(3*pos, color)
            self.grid[3].set_pixel(3*pos-1, color)
            self.grid[4].set_pixel(3*pos+1, color)
            self.grid[4].set_pixel(3*pos, color)
        elif num == 3:
            self.grid[0].set_pixel(3*pos, color)
            self.grid[0].set_pixel(3*pos-1, color)
        
            #self.grid[1].set_pixel(3*pos+1, color)
            #self.grid[1].set_pixel(3*pos, color)
            self.grid[1].set_pixel(3*pos-1, color)
        
            self.grid[2].set_pixel(3*pos, color)
            self.grid[2].set_pixel(3*pos-1, color)

            #self.grid[3].set_pixel(3*pos+1, color)
            #self.grid[3].set_pixel(3*pos, color)
            self.grid[3].set_pixel(3*pos-1, color)
            self.grid[4].set_pixel(3*pos+1, color)
            self.grid[4].set_pixel(3*pos, color)
        elif num == 4:
            self.grid[0].set_pixel(3*pos, color)
            #self.grid[0].set_pixel(3*pos-1, color)
        
            #self.grid[1].set_pixel(3*pos+1, color)
            self.grid[1].set_pixel(3*pos, color)
            #self.grid[1].set_pixel(3*pos-1, color)
        
            self.grid[2].set_pixel(3*pos, color)
            self.grid[2].set_pixel(3*pos-1, color)

            self.grid[3].set_pixel(3*pos+1, color)
            #self.grid[3].set_pixel(3*pos, color)
            self.grid[3].set_pixel(3*pos-1, color)
            self.grid[4].set_pixel(3*pos+1, color)
            
            
        elif num == 5:
            self.grid[0].set_pixel(3*pos, color)
            self.grid[0].set_pixel(3*pos-1, color)
        
            #self.grid[1].set_pixel(3*pos+1, color)
            #self.grid[1].set_pixel(3*pos, color)
            self.grid[1].set_pixel(3*pos-1, color)
        
            self.grid[2].set_pixel(3*pos, color)
            self.grid[2].set_pixel(3*pos-1, color)

            self.grid[3].set_pixel(3*pos+1, color)
            #self.grid[3].set_pixel(3*pos, color)
            #self.grid[3].set_pixel(3*pos-1, color)
            
            self.grid[4].set_pixel(3*pos+1, color)
            self.grid[4].set_pixel(3*pos, color)
        elif num == 6:
            self.grid[0].set_pixel(3*pos, color)
            self.grid[0].set_pixel(3*pos-1, color)
        
            self.grid[1].set_pixel(3*pos+1, color)
            #self.grid[1].set_pixel(3*pos, color)
            self.grid[1].set_pixel(3*pos-1, color)
        
            self.grid[2].set_pixel(3*pos, color)
            self.grid[2].set_pixel(3*pos-1, color)

            self.grid[3].set_pixel(3*pos+1, color)
            #self.grid[3].set_pixel(3*pos, color)
            #self.grid[3].set_pixel(3*pos-1, color)
            
            self.grid[4].set_pixel(3*pos+1, color)
            self.grid[4].set_pixel(3*pos, color)
        elif num == 7:
            self.grid[0].set_pixel(3*pos, color)
            #self.grid[0].set_pixel(3*pos-1, color)
        
            #self.grid[1].set_pixel(3*pos+1, color)
            self.grid[1].set_pixel(3*pos, color)
            #self.grid[1].set_pixel(3*pos-1, color)
        
            #self.grid[2].set_pixel(3*pos, color)
            self.grid[2].set_pixel(3*pos-1, color)

            #self.grid[3].set_pixel(3*pos+1, color)
            #self.grid[3].set_pixel(3*pos, color)
            self.grid[3].set_pixel(3*pos-1, color)
            self.grid[4].set_pixel(3*pos+1, color)
            self.grid[4].set_pixel(3*pos, color)
            self.grid[4].set_pixel(3*pos-1, color)
        elif num == 8:
            self.grid[0].set_pixel(3*pos, color)
            self.grid[0].set_pixel(3*pos-1, color)
        
            self.grid[1].set_pixel(3*pos+1, color)
            #self.grid[1].set_pixel(3*pos, color)
            self.grid[1].set_pixel(3*pos-1, color)
        
            self.grid[2].set_pixel(3*pos, color)
            self.grid[2].set_pixel(3*pos-1, color)

            self.grid[3].set_pixel(3*pos+1, color)
            #self.grid[3].set_pixel(3*pos, color)
            self.grid[3].set_pixel(3*pos-1, color)
            self.grid[4].set_pixel(3*pos+1, color)
            self.grid[4].set_pixel(3*pos, color)
        elif num == 9:
            self.grid[0].set_pixel(3*pos, color)
            self.grid[0].set_pixel(3*pos-1, color)
        
            #self.grid[1].set_pixel(3*pos+1, color)
            #self.grid[1].set_pixel(3*pos, color)
            self.grid[1].set_pixel(3*pos-1, color)
        
            self.grid[2].set_pixel(3*pos, color)
            self.grid[2].set_pixel(3*pos-1, color)

            self.grid[3].set_pixel(3*pos+1, color)
            #self.grid[3].set_pixel(3*pos, color)
            self.grid[3].set_pixel(3*pos-1, color)
            
            self.grid[4].set_pixel(3*pos+1, color)
            self.grid[4].set_pixel(3*pos, color)
            
        self.show()
        

    def show_gradient(self):
        if self.display_type != "gradient":
            for i in self.grid:
                i.brightness(self.brightness)

        self.display_type = "gradient"
        
        red = (255, 0, 0)
        orange = (255, 50, 0)
        yellow = (255, 100, 0)
        green = (0, 255, 0)
        blue = (0, 0, 255)
        indigo = (100, 0, 90)
        violet = (200, 0, 100)
        colors_rgb = [red, orange, yellow, green, blue, indigo, violet]

        # same colors as normaln rgb, just 0 added at the end
        colors_rgbw = [color+tuple([0]) for color in colors_rgb]
        colors_rgbw.append((0, 0, 0, 255))

        # uncomment colors_rgbw if you have RGBW strip
        colors = colors_rgb
        # colors = colors_rgbw

        step = round(self.pixels / len(colors))
        current_pixel = 0

        for color1, color2 in zip(colors, colors[1:]):
            for i in self.grid:
                i.set_pixel_line_gradient(current_pixel, current_pixel + step, color1, color2)
            current_pixel += step

        for i in self.grid:
            i.set_pixel_line_gradient(current_pixel, self.pixels - 1, violet, red)

        self.deadline = time.ticks_add(time.ticks_ms(), self.tickupdate)
        print("Initialized")
        
        self.show()
        
    def update(self):
        if time.ticks_diff(self.deadline, time.ticks_ms()) < 0:
            self.deadline = time.ticks_add(time.ticks_ms(), self.tickupdate)
            if self.display_type == "gradient":
                for i in self.grid:
                    i.rotate_right(1)
            
                self.show()
        if self.display_type == "clear":
            self.clear()

d = Display()

d.clear()


# if you want to show numbers:
#for i in range(0,9):
#    d.show_number(4, i, (255,0,0,0))
#    d.show_number(3, i+1%10, (255,255,0,0))
#    d.show_number(2, i+2%10, (0,0,255,0))
#    time.sleep(1)

d.show_gradient()

deadline = time.ticks_add(time.ticks_ms(), 15000)
button = Pin(21, Pin.IN, Pin.PULL_UP)

cur_value = 1
active = 0

while True:
    d.update()
    time.sleep(0.001)
    
    value = button.value()
    if value != cur_value:
        active = active + 1
    else:
        active = 0
    
    if active > 100:
        if value == 0:
            d.clear()
        elif value == 1:
            d.show_gradient()
            
        cur_value = button.value()
        active = 0
        

