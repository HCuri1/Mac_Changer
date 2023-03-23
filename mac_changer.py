# /usr/bin/env python

import subprocess

print("---- MAC Changer ----\n\n")


interface=str(input("Interface: ")).strip()

print("\n\n- Keep it blank to a random one")
print("- Type 'd' for the original\n\n")

newMac=str(input("New Mac: ")).strip()

subprocess.call(["ifconfig", interface, "up"])
subprocess.call(["ifconfig", interface, "hw", "ether", newMac])
subprocess.call(["ifconfig", interface, "up"])

print(f"\n[+] {interface} MAC Adress changed to {newMac}")