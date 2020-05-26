#!/usr/bin/env python3

import os
import time
import modules.test as test
from modules.led import LedControl

RED = (255, 0, 0, 0)
GREEN = (0, 255, 0, 0)
BLUE = (0, 0, 255, 0)


if __name__ == "__main__":
    while True:
        # Read pot values
        # Handle change
        print("test")
        time.sleep(1)
        LedControl.change_color(RED)
        time.sleep(1)
        LedControl.change_color(GREEN)
        time.sleep(1)
        LedControl.change_color(BLUE)





