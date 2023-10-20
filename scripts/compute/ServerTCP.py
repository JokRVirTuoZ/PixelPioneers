import socket
from threading import Thread
import time
from socketserver import ThreadingMixIn


# Programme du serveur TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("100.84.214.153", 8888))
mythreads = []

def decode(string):
    if string.type != str:
        string = str(string)
    if string[0] == "/":
        a = string[1]
        b = string[2]
        if a == "w":#chuchoter
            pass
        if a == "i":#inventory
            pass
        if a == "m":#move int int
            pass
        if a == "a":#action parmis un choix int
            pass
        if a == "extorquer":#voler un montant à quelq'un
            pass
        if a == "warp":#x y voyage rapide
            pass
        if a == "search":#fouiller la zone
            pass
        if a == "charm":#charmer l'entité sur la case
            pass
        if a == "run":#s'enfuire
            pass
        if a == "sleep":#endormir
            pass










class myThread(Thread):
    def __init__(self, ip, port):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.name = ""
        self.sleeped = False
        print("[+] Nouveau thread démarré pour " + ip + ":" + str(port) + " as " + self.name)

    def run(self):
        if self.name == "" :
            data = con.recv(2048)
            self.name = data.decode("UTF-8")
        while True:
            data = con.recv(2048)
            data = data.decode("UTF-8")
            print(self.name, ":", data)
            if data == 'close':
                self.sleeped = True
                while self.sleeped:
                    try:
                        data = con.recv(2048)
                        data = data.decode("UTF-8")
                        if data and data != 'close':
                            print(self.name, "reconnected", data)
                            self.sleeped = False
                        time.sleep(10)
                    except:
                        time.sleep(10)
                    else:
                        if data:
                            print(self.name, ":", data)


while True:
    s.listen(5)
    print("Serveur: en attente de connexions des clients TCP ...")
    (con, (ip, port)) = s.accept()
    flag = False
    for i in mythreads:
        if i.ip == ip:
            print(f"trouver un compte déja existant : ")
            mythread = i
            flag = True
    if not flag:
        mythread = myThread(ip, port)
        mythread.start()
        mythreads.append(mythread)

for t in mythreads:
    t.join()
