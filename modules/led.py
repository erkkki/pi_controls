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

    def __init__(self):
        self.strip = neopixel.NeoPixel(
            self.LED_PIN,
            self.LED_COUNT,
            brightness=self.LED_BRIGHTNESS,
            auto_write=False,
            pixel_order=self.LED_ORDER
        )
        # [(255, 0, 0), (255, 3, 0),
        self.colors = pickle.load(open("wawelength.pickle", "rb"))

    def set_brightness(self, val):
        self.LED_BRIGHTNESS = val

    def get_color(self, val):
        color = (
            self.colors[val][0],
            self.colors[val][1],
            self.colors[val][2],
            0
        )
        return self.colors[val]

    def change_color(self, val):
        color = self.get_color(val)
        self.strip.fill(color)
        self.strip.show()
