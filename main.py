#!/usr/bin/env python3

import os
import time
import modules.test as test
from modules.led import LedControl
from modules.potentiometer import PotControl

led = LedControl()
pot = PotControl()

fps = [
    1/120,
    1/60,
    1/30,
]


def led_test():
    for x in range(99):
        led.color_wheel_update()
        time.sleep(fps[0])


def pot_test():
    time.sleep(1)
    values = pot.get_pot_values()
    print(values)


if __name__ == "__main__":
    while True:
        led_test()







