import socket as suck
import time
import threading

s = suck.socket(suck.AF_INET, suck.SOCK_STREAM)
def ConnectToServer():
    s.connect(("100.84.214.153", 8888))
    time.sleep(1)
    threadListen = threading.Thread(target=listen)
    threadListen.start()


def sendString(string):
    if threadListen.is_alive():
        threadListen.join()
    s.send(string.encode("UTF-8"))
    if string == "close":
        s.close()
def listen():
    while 1:
        bf = ""
        bf = s.recv(2048).decode("UTF-8")
        if bf != "":
            print(f"\n"+bf+"\n")
        time.sleep(0.2)


threadListen = threading.Thread(target=listen)
