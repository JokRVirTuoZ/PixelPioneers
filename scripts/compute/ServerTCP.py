import socket
from threading import Thread
import time

# Programme du serveur TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("100.84.214.153", 8888))
mythreads = []


def decodeMsg(user, string, mythreads):
    if type(string) != str:
        string = str(string)
    if string[0] == "/":
        text = string.split()
        a = text[0][1:]
        if a == "w":  # chuchoter
            flag = False
            for i in mythreads:
                if i.name == text[1]:
                    print("ok3")
                    msg = ""
                    flag = True
                    for y in range(len(text) - 2):
                        msg += text[2 + y] + " "
                    i.socket.send(f"Message from {user.name} : {msg}".encode("UTF-8"))
            if not flag:
                i.socket.send(f"Le contact {text[1]} n'as pas été trouvé".encode("UTF-8"))
        if a == "i":  # inventory
            pass
        if a == "m":  # move int int
            pass
        if a == "a":  # action parmis un choix int
            pass
        if a == "extorquer":  # voler un montant à quelq'un
            pass
        if a == "warp":  # x y voyage rapide
            pass
        if a == "search":  # fouiller la zone
            pass
        if a == "charm":  # charmer l'entité sur la case
            pass
        if a == "run":  # s'enfuire
            pass
        if a == "sleep":  # endormir
            pass
        if a == "tabasserjusquacequemortsensuive":  # bagare
            flag = False
            for i in mythreads:
                if i.name == text[1]:
                    print("ok4")
                    flag = True
                    i.socket.send(f"{user.name} t'as tabasserjusquacequemortsensuive".encode("UTF-8"))
                    time.sleep(2)
                    i.closed()
            if not flag:
                i.socket.send(f"Le contact {text[1]} n'as pas été trouvé".encode("UTF-8"))



class myThread(Thread):
    def __init__(self, socket, ip, port):
        Thread.__init__(self)
        self.socket = socket
        self.ip = ip
        self.port = port
        self.name = ""
        self.sleeped = False
        print("[+] Nouveau thread démarré pour " + ip + ":" + str(port) + " as " + self.name)

    def run(self):
        while True:
            if self.name == "":
                data = self.socket.recv(2048)
                data = data.decode("UTF-8")
                if " " in data:
                    self.socket.send(b"Votre nom ne peut pas comportez d'espace")
                else:
                    self.name = data
                    break
        while True:
            data = self.socket.recv(2048)
            data = data.decode("UTF-8")
            print(self.name, ":", data)
            decodeMsg(self, data, mythreads)
            if data == 'close':
                self.sleeped = True
                while self.sleeped:
                    try:
                        data = self.socket.recv(2048)
                        data = data.decode("UTF-8")
                        if data and data != 'close':
                            print(self.name, "reconnected")
                            print(self.name, ":", data)
                            decodeMsg(self, data, mythreads)
                            self.sleeped = False
                            data = ""
                        else:
                            time.sleep(10)
                    except:
                        time.sleep(10)
                    else:
                        if data:
                            print(self.name, ":", data)
                            decodeMsg(self, data, mythreads)
    def closed(self):
        self.socket.shutdown()
        self.socket.close()

    def reopen(self):
        time.sleep(0.0025)
        self.socket.connect((self.ip, self.port))


while True:
    s.listen(5)
    print("Serveur: en attente de connexions des clients TCP ...")
    (con, (ip, port)) = s.accept()
    flag = False
    for i in mythreads:
        if i.ip == ip:
            print(f"trouver un compte déja existant : " + i.name)
            flag = True
            i.socket = con
            i.ip = ip
            i.port = port
            i.closed()
            i.reopen()
    if not flag:
        con.send(b"Veuillez rentrer votre pseudo")
        mythread = myThread(con, ip, port)
        mythread.start()
        mythreads.append(mythread)

for t in mythreads:
    t.join()
