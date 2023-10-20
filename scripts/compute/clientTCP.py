import socket as suck
import time

s = suck.socket(suck.AF_INET, suck.SOCK_STREAM)
def ConnectToServer():
    s.connect(("100.84.214.153", 8888))
    #time.sleep(1)

def sendString(string):
    s.send(string.encode("UTF-8"))
    if string == "close":
        s.close()
