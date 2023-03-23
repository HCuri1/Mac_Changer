# /usr/bin/env python

import subprocess

print("---- MAC Changer ----\n\n")


interface=str(input("Interface: ")).strip()

print("\n\n- Keep it blank to a random one")
print("- Type 'd' for the original\n\n")

newMac=str(input("New Mac: ")).strip()

subprocess.call(f"ifconfig {interface} down", shell=True)
subprocess.call(f"ifconfig {interface} hw ether {newMac}", shell=True)
subprocess.call(f"ifconfig {interface} up", shell=True)

print(f"[+] {interface} MAC Adress changed to {newMac}")