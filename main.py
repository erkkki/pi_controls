#!/usr/bin/env python3

import os
import time
import modules.test as test
from modules.led import LedControl
from modules.potentiometer import PotControl

RED = (255, 0, 0, 0)
GREEN = (0, 255, 0, 0)
BLUE = (0, 0, 255, 0)
led = LedControl()
pot = PotControl()


def led_test():
    time.sleep(1)
    led.change_color(RED)
    time.sleep(1)
    led.change_color(GREEN)
    time.sleep(1)
    led.change_color(BLUE)


def pot_test():
    time.sleep(1)
    values = pot.get_pot_values()
    print(values)


if __name__ == "__main__":
    while True:
        pot_test()







