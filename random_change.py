from subprocess import call

def randomChange(interface):
    
    call("./random_changer.sh", interface)