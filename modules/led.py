#!/usr/bin/env python3

# import board
# import neopixel


# Handle led brightness & color change.
class LedControl:
    # LED strip configuration:
    LED_COUNT = 20  # Number of LED pixels.
    # LED_PIN = board.D21  # GPIO pin
    LED_BRIGHTNESS = 0.1  # LED brightness
    LED_MIN_BRIGHTNESS = 0.0
    LED_MAX_BRIGHTNESS = 0.9
    # LED_ORDER = neopixel.GRBW  # order of LED colours. May also be RGB, GRBW, or RGBW
    strip = ''

    def __init__(self):
        self.strip = ''
        # self.strip = neopixel.NeoPixel(
        #    self.LED_PIN,
        #    self.LED_COUNT,
        #    brightness=self.LED_BRIGHTNESS,
        #    auto_write=False,
        #    pixel_order=self.LED_ORDER
        # )

    def set_brightness(self, val):
        self.LED_BRIGHTNESS = val
