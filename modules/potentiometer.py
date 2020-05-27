#!/usr/bin/env python3

import board
import digitalio
import busio
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn


# Read pin values from mcp3008
class PotControl:
    def __init__(self):
        self.spi = busio.SPI(
            clock=board.SCK,
            MISO=board.MISO,
            MOSI=board.MOSI
        )
        self.cs = digitalio.DigitalInOut(board.D22)
        self.mcp = MCP.MCP3008(self.spi, self.cs)
        self.pins = [
            AnalogIn(self.mcp, MCP.P0),
            AnalogIn(self.mcp, MCP.P1),
            AnalogIn(self.mcp, MCP.P2),
        ]
        self.values = [0, 0, 0]
        self.margin = 400
        self.read_pot_values()

    def get_pot_values(self):
        # read and update values.
        self.read_pot_values()
        return self.values

    def read_pot_values(self):
        # read the analog pins
        values = []
        for pin in self.pins:
            values.append(pin.value)
        for x in range(3):
            if values[x] > self.values[x]+self.margin or values[x] < self.values[x]-self.margin:
                self.values[x] = values[x]
        return True
