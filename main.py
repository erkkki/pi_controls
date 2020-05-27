#!/usr/bin/env python3

import time
import threading
from modules.led import LedControl
from modules.potentiometer import PotControl

led = LedControl(65535)
pot = PotControl()

threads = list()
pot_values = [0, 0, 0]


def led_thread():
    while True:
        led.change_strip_color(pot_values[0])
        time.sleep(0.001)


def pot_thread():
    global pot_values
    while True:
        pot_values = pot.get_pot_values()
        time.sleep(0.001)


def create_threads():
    x = threading.Thread(target=led_thread, args=(), daemon=True)
    threads.append(x)
    x.start()

    x = threading.Thread(target=pot_thread, args=(), daemon=True)
    threads.append(x)
    x.start()


if __name__ == "__main__":
    create_threads()
    while True:
        print(pot_values)
        time.sleep(1)







