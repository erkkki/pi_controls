#!/usr/bin/env python3

import time
import threading
from modules.led import LedControl
from modules.potentiometer import PotControl
from modules.volume import VolumeControl

led = LedControl(65535)
pot = PotControl()
volume = VolumeControl(65535)

threads = list()
pot_values = [0, 0, 0]


def led_thread():
    margin = 1000
    old_values = pot_values
    while True:
        old_value = pot_values[0]
        if old_values[0] > pot_values[0]+margin or old_values[0] < pot_values[0]-margin:
            led.set_color(pot_values[0])
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


def pot_thread():
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
        print(pot_values)
        time.sleep(1)







