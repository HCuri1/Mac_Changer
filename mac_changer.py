# /usr/bin/env python

import subprocess
import default_change
import check_mac
import random_change

print("---- MAC Changer ----\n\n")


interface=str(input("Interface: ")).strip()

print("\n\n- Keep it blank to a random one")
print("- Type 'd' for the original\n\n")

newMac=str(input("New Mac: ")).strip()

if not newMac:
    
    random_change.randomChange(interface)
    
elif (newMac=="d"):
    
    default_change.defaultChange(interface)

else:
    
    if check_mac.checkMac(newMac) == True:
        
        subprocess.call(["./changer.sh", interface, newMac])
        
    else:
        
        print("Invalid MAC Adress!")


print(f"\n[+] {interface} MAC Adress changed to {newMac}")