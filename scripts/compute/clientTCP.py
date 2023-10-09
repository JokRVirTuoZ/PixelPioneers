import socket as suck
import time

def ConnectToServer():
    s = suck.socket(suck.AF_INET, suck.SOCK_STREAM)
    s.connect(("172.23.5.234", 4258))
    test = "PixelPioneer".encode()
    close = "close".encode()
    s.send(test)
    time.sleep(1)
    s.send(close)
    s.close()
