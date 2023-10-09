import socket as suck
import time

s = suck.socket(suck.AF_INET, suck.SOCK_STREAM)
def ConnectToServer():
    s.connect(("172.23.5.234", 4258))
    test = "PixelPioneer".encode()
    s.send(test)
    time.sleep(1)

def sendString(string):
    s.send(string.encode("UTF-8"))
    if string == "close":
        s.close()
