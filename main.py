#!/usr/bin/env python3

import os
import time
import modules.test as test
from modules.led import LedControl
from modules.potentiometer import PotControl

led = LedControl()
pot = PotControl()


def led_test():
    for x in range(99):
        led.change_color(x)
        time.sleep(1)


def pot_test():
    time.sleep(1)
    values = pot.get_pot_values()
    print(values)


if __name__ == "__main__":
    while True:
        led_test()







