#!/usr/bin/env python3

import time
import board
import digitalio
import busio
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn


# Read potentiometer values and check if value has changed.
class PotControl:

    def __init__(self):
        self.spi = busio.SPI(
            clock=board.SCK,
            MISO=board.MISO,
            MOSI=board.MOSI
        )
        self.cs = digitalio.DigitalInOut(board.D22)
        self.mcp = MCP.MCP3008(self.spi, self.cs)
        self.values = [
            AnalogIn(self.mcp, MCP.P0),
            AnalogIn(self.mcp, MCP.P1),
            AnalogIn(self.mcp, MCP.P2),
        ]

    def get_pot_values(self):
        return self.values

    def read_pot_values(self):
        return True
