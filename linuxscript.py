#! /usr/bin/env python

import subprocess
import time

subprocess.call(["gsettings", "set", "org.cinnamon.desktop.wm.preferences", "titlebar-font", "Sans 10"])

subprocess.call(["timedatectl", "set-timezone", "Canada/Eastern"])


subprocess.call(["gsettings", "set", "org.cinnamon.desktop.interface", "text-scaling-factor", "2"])

subprocess.call(["sudo", "apt-get", "install", "libxss1", "libappindicator1", "libindicator7"])

subprocess.call(["wget", "https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb"])

subprocess.call(["sudo", "dpkg", "-i", "google-chrome-stable_current_amd64.deb"])

