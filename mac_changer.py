# /usr/bin/env python

import subprocess
import optparse
import default_change
import random_change

subprocess.call(["chmod", "+x", "changer.sh"])
subprocess.call(["chmod", "+x", "default_changer.sh"])
subprocess.call(["chmod", "+x", "random_changer.sh"])

parser=optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface", default="", help="set interface to change the MAC adress")
parser.add_option("-d", "--default", action="store_true", dest="default", default=False, help="return the interface to the original MAC Adress")
parser.add_option("-m", "--mac", dest="newMac", default="", help="set the new MAC Adress (if not set, a random one will be set)")

(options, arguments) = parser.parse_args()

interface=str(options.interface).strip()
newMac=str(options.newMac).strip()
default=options.default

print("---- MAC Changer ----\n\n")

if not interface:
    
    print("[ERROR] Set an interface!")

else:
    if default:
        
        default_change.defaultChange(interface)
        
    elif not newMac:
        
        random_change.randomChange(interface)

    else:
            
        subprocess.call(["./changer.sh", interface, newMac])
            