# Mac_Changer
Python program to change an interface MAC Adress 

# Requirements
- macchanger

For Debian-based linux distros, it can be installed by:
```
apt-get install macchanger
```

# How to execute this program:

Must be executed as sudo

```
python3 mac_changer.py [options]
```

# Program options:

-h, --help            show help message and exit

-i INTERFACE, --interface=INTERFACE
                    set interface to change the MAC adress

-d, --default       return the interface to the original MAC Adress

-m NEWMAC, --mac=NEWMAC
                    set the new MAC Adress (if not set, a random one will
                    be set)