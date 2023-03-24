from subprocess import call

def defaultChange (interface):
    
    call(["./default_changer.sh", interface])