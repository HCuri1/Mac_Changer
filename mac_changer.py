# /usr/bin/env python

import subprocess

interface=str(input("Interface: ")).strip()
newMac=str(input("New Mac (keep it blank for random): ")).strip()

subprocess.call(f"ifconfig {interface} down", shell=True)
subprocess.call(f"ifconfig {interface} hw ether {newMac}", shell=True)
subprocess.call(f"ifconfig {interface} up", shell=True)