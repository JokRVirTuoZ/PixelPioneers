import socket
from threading import Thread
from socketserver import ThreadingMixIn


class myThread(Thread):
    def __init__(self, ip, port):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        name = ""
        print("[+] Nouveau thread démarré pour " + ip + ":" + str(port) +" as " + self.name)

    def run(self):
        data = con.recv(2048)
        self.name = data.decode("UTF-8")
        while True:
            data = con.recv(2048)
            data = data.decode("UTF-8")
            print(self.name,":", data)
            if data == 'exit':
                break


# Programme du serveur TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('127.0.0.1', 8888))
mythreads = []

while True:
    s.listen(5)
    print("Serveur: en attente de connexions des clients TCP ...")
    (con, (ip, port)) = s.accept()
    mythread = myThread(ip, port)
    mythread.start()
    mythreads.append(mythread)

for t in mythreads:
    t.join()