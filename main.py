#!/usr/bin/env python3

import time
import threading
from modules.led import LedControl
from modules.potentiometer import PotControl
from modules.volume import VolumeControl

POT_MAX_VAL = 65535
led = LedControl(POT_MAX_VAL)
pot = PotControl()
volume = VolumeControl(POT_MAX_VAL)
threads = list()
pot_values = [0, 0, 0]


def led_thread():
    margin = 1000
    old_values = pot_values
    while True:
        if old_values[0] > pot_values[0] + margin or old_values[0] < pot_values[0] - margin:
            led.update(pot_values[0])
        elif pot_values[0] > 50000:
            led.update(pot_values[0])

        if old_values[1] > pot_values[1] + margin or old_values[1] < pot_values[1] - margin:
            led.set_brightness(pot_values[1])

        old_values = pot_values
        time.sleep(0.04)


def volume_thread():
    margin = 1000
    old_values = pot_values
    while True:
        if old_values[2] > pot_values[2] + margin or old_values[2] < pot_values[2] - margin:
            volume.set_volume(pot_values[2])

        old_values = pot_values
        time.sleep(0.1)


def pot_thread(): # Read potentiometer values from mcp3008
    global pot_values
    while True:
        pot_values = pot.get_pot_values()
        time.sleep(0.04)


def create_threads():
    x = threading.Thread(target=led_thread, args=(), daemon=True)
    threads.append(x)
    x.start()

    x = threading.Thread(target=pot_thread, args=(), daemon=True)
    threads.append(x)
    x.start()

    x = threading.Thread(target=volume_thread, args=(), daemon=True)
    threads.append(x)
    x.start()


if __name__ == "__main__":
    create_threads()
    while True:
        time.sleep(1)







