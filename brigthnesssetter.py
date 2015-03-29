#!/usr/bin/env python

import os

class BrightnessSetter:
  def set_brightness(self, level) :
    os.system("echo " + str(level) + " | sudo tee /sys/class/backlight/intel_backlight/brightness");

