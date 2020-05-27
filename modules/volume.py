#!/usr/bin/env python3

import os


class VolumeControl:
    def __init__(self, max_val):
        self.volume = 10
        self.max_val = max_val
        self.update_volume()

    def set_volume(self, volume):
        volume = self.range_remap(volume, 100)
        self.volume = volume
        self.update_volume()

    def update_volume(self):
        set_vol_cmd = 'sudo amixer cset numid=1 -- {volume}% > /dev/null' \
            .format(volume=self.volume)
        os.system(set_vol_cmd)

    def range_remap(self, val, max_val):
        val = val / self.max_val
        return val * max_val
