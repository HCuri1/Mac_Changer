from subprocess import call

def defaultChange (interface):
    call(["macchanger", "-p", interface])