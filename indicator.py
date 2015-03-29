#!/usr/bin/env python

import sys
import gtk
import appindicator
import brigthnesssetter as bs;

class SetBrightnessIndicator:


    def __init__(self):
        self.ind = appindicator.Indicator("set-brigthness-indicator",
                                           "icon-brightness.png",
                                           appindicator.CATEGORY_APPLICATION_STATUS)
        self.ind.set_status(appindicator.STATUS_ACTIVE)

        self.menu_setup()
        self.ind.set_menu(self.menu)
	self.bs = bs.BrightnessSetter()

    def main(self):
        gtk.main()

    def menu_setup(self):
        self.menu = gtk.Menu()

        self.dark_item = gtk.MenuItem("Dark")
        self.dark_item.connect("activate", self.dark)
        self.dark_item.show()
        self.menu.append(self.dark_item)

        self.light_item = gtk.MenuItem("Light")
        self.light_item.connect("activate", self.light)
        self.light_item.show()
        self.menu.append(self.light_item)

        self.quit_item = gtk.MenuItem("Quit")
        self.quit_item.connect("activate", self.quit)
        self.quit_item.show()
        self.menu.append(self.quit_item)

    def dark(self, widget):
        self.bs.set_brightness(1000)
 
    def light(self, widget):
        self.bs.set_brightness(4000)

    def quit(self, widget):
        sys.exit(0)

if __name__ == "__main__":
    indicator = SetBrightnessIndicator()
    indicator.main()
