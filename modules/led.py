#!/usr/bin/env python3

import pickle
import board
# https://learn.adafruit.com/adafruit-neopixel-uberguide/python-circuitpython
# https://circuitpython.readthedocs.io/projects/neopixel/en/latest/api.html
import neopixel


# Handle led brightness & color change.
class LedControl:
    # LED strip configuration:
    LED_COUNT = 22  # Number of LED pixels.
    # On the Raspberry Pi, NeoPixels must be connected to GPIO10, GPIO12, GPIO18 or GPIO21 to work!
    LED_PIN = board.D21  # GPIO pin
    LED_BRIGHTNESS = 0.1  # LED brightness
    LED_MIN_BRIGHTNESS = 0.0
    LED_MAX_BRIGHTNESS = 0.9
    LED_ORDER = neopixel.GRBW  # order of LED colours. May also be RGB, GRBW, or RGBW
    WAWELENGTH = "/home/pi/Documents/pi_controls/modules/wawelength.pickle" # map of different colors. https://github.com/erkkki/wawelength
    pos = 0
    dir = True

    def __init__(self, max_val):
        self.strip = neopixel.NeoPixel(
            self.LED_PIN,
            self.LED_COUNT,
            brightness=self.LED_BRIGHTNESS,
            auto_write=False,
            pixel_order=self.LED_ORDER
        )
        # inside pickle = [(255, 0, 0), (255, 3, 0),
        self.colors = pickle.load(
            open(self.WAWELENGTH, "rb")
        )
        self.colors_len = len(self.colors)-1
        self.max_val = max_val

    def update(self, val):
        if val > 50000:
            self.color_wheel_update()
        else:
            self.set_color(val)
        return True

    def set_brightness(self, val):
        if val > 1:
            val = self.range_remap(val, self.LED_MAX_BRIGHTNESS)

        self.LED_BRIGHTNESS = val
        self.update_strip()
        return True

    def get_color(self, val):
        color = (
            self.colors[val][0],
            self.colors[val][1],
            self.colors[val][2],
            0
        )
        return color

    def update_strip(self):
        self.strip.brightness = self.LED_BRIGHTNESS
        self.strip.show()

    def range_remap(self, val, max_val):
        val = val / self.max_val
        return val * max_val

    def set_color(self, val):
        val = self.range_remap(val, self.colors_len)
        color = self.get_color(int(val))
        self.strip.fill(color)
        self.update_strip()

    def color_wheel_update(self):
        for x in range(self.LED_COUNT):
            if self.dir:
                color_pos = self.pos + x
            else:
                color_pos = self.pos - x
            if color_pos >= self.colors_len:
                self.dir = False
                color_pos = self.colors_len
            if color_pos <= 0:
                self.dir = True
                color_pos = 0
            self.strip[x] = self.get_color(color_pos)
            self.pos = self.pos + 1
        self.update_strip()
