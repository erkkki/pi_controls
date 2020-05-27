#!/usr/bin/env python3

import pickle
import board
import neopixel


# Handle led brightness & color change.
class LedControl:
    # LED strip configuration:
    LED_COUNT = 22  # Number of LED pixels.
    LED_PIN = board.D21  # GPIO pin
    LED_BRIGHTNESS = 0.1  # LED brightness
    LED_MIN_BRIGHTNESS = 0.0
    LED_MAX_BRIGHTNESS = 0.9
    LED_ORDER = neopixel.GRBW  # order of LED colours. May also be RGB, GRBW, or RGBW
    WAWELENGTH = "./modules/wawelength.pickle"
    pos = 0

    def __init__(self):
        self.strip = neopixel.NeoPixel(
            self.LED_PIN,
            self.LED_COUNT,
            brightness=self.LED_BRIGHTNESS,
            auto_write=False,
            pixel_order=self.LED_ORDER
        )
        # inside pickle = [(255, 0, 0), (255, 3, 0),
        self.colors = pickle.load(open(self.WAWELENGTH, "rb"))

    def set_brightness(self, val):
        self.LED_BRIGHTNESS = val

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

    def change_color(self, val):
        color = self.get_color(val)
        self.strip.fill(color)
        self.strip.show()

    def color_wheel_update(self):
        for x in range(self.LED_COUNT):
            self.strip[x] = self.get_color(self.pos + x)
            self.strip.show()
        self.pos = self.pos + 1
        if self.pos > len(self.colors):
            self.pos = 0
