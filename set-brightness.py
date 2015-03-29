#!/usr/bin/env python

import sys
import brigthnesssetter as bs

brightness = int(sys.argv[1])

bSetter = bs.BrightnessSetter()

if brightness >= 500 and brightness <= 5000:
  bSetter.set_brightness(brightness)
