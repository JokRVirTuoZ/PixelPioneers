import socket
from threading import Thread
from time import sleep
from scripts._class.User import User


def clientHandler(user):
    user.connection()
    user.client.setblocking(False)
    msg=b""
    try:
        msg = user.client.recv(1024)
    except Exception as e:
        print(e)
    if msg != b'':
        msg = msg.decode("UTF-8")
    else:
        #user.client.close()
        pass
    if user.name == "":
        User.name = msg
    while True:
        msg = b""
        try:
            msg = user.client.recv(1024)
        except Exception as e:
            pass
        if msg != b'' and type(msg) == bytes:
            msg = msg.decode("UTF-8")
            # do some checks and if msg == someWeirdSignal: break:
            print(f"{user.name}({user.ip},{user.port}) : {msg}")
        # Maybe some code to compute the last digit of PI, play game or anything else can go here and when you are done.
        #clientsocket.send(msg)
        if msg == "close":
            break
        sleep(1)
    #print(f"Une erreur est survenue avec {user.name} : {e}")
    user.deconnection()
    print(f"Le client : {User.name} s'est déconnecté")
    user.client.close()

ADRESSE = ''
PORT = 8888
serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serveur.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 2)
serveur.bind((ADRESSE, PORT))
serveur.listen(10)
tab = []
threads = []
while True:
    client, adresseClient = serveur.accept()
    retur = False
    for i in tab:
        if adresseClient[0] == i.ip:
            retur = True
            break
    if not retur:
        user = User(client, adresseClient, len(tab))
        tab.append(user)
    else:
        user = i
        user.client = client
        user.port = adresseClient[1]
    print(f'Connexion de {adresseClient}, {retur}')
    thread = Thread(target=clientHandler(user))
    print("ok1")
    try:
        print("ok2")
        for i in threads:
            i.join()
    except Exception as e:
        print(e)
    print("ok3")
    thread.start()
    print("ok4")
    threads.append(thread)
    print(threads)


for i in threads:
    i.join()

for i in tab:
    tab.client.close()
    print('Fermeture de la connexion avec le client: ',+tab.name)
print('Arret du serveur.')
serveur.close()