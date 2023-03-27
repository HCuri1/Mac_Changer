from subprocess import run

def defaultChange (interface):
    
    output = run(["./default_changer.sh", interface], capture_output=True).stdout
                    
    if "New MAC" not in str(output):
            
        print("[-] Invalid interface!")
            
    else:
                
        print(output)
        print(f"\n[+] {interface} MAC Address changed!")