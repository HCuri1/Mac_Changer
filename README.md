# Mac_Changer
Python program to change an interface MAC Address 

# Requirements
- macchanger

For Debian-based linux distros, it can be installed by:
```
apt-get install macchanger
```

# How to execute this program:
```
python3 mac_changer.py [options]
```
Must be executed as sudo

# Program options:
```
-h, --help            show help message and exit

-i INTERFACE, --interface=INTERFACE
                    set interface to change the MAC address

-d, --default       return the interface to the original MAC Address

-m NEWMAC, --mac=NEWMAC
                    set the new MAC Address (if not set, a random one will
                    be set)
```
