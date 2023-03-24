from subprocess import call

def defaultChange (interface):
    
    call(["./default_changer.sh", interface])
    print(f"\n[+] {interface} MAC Address changed!")