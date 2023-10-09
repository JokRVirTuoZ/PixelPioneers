import socket
from threading import Thread

from scripts._class.User import User


def clientHandler(User):
    User.connection()
    msg = User.client.recv(1024)
    if msg != b'':
        msg = msg.decode("UTF-8")
    else:
        User.client.close()
    if User.name == "":
        User.name = msg
    try:
        while True:
            msg = User.client.recv(1024)
            if msg != b'':
                msg = msg.decode("UTF-8")
            # do some checks and if msg == someWeirdSignal: break:
            print(f"{User.name}({User.ip},{User.port}) : {msg}")
            # Maybe some code to compute the last digit of PI, play game or anything else can go here and when you are done.
            #clientsocket.send(msg)
            if msg == "close":
                break
    except Exception as e:
        print(f"Une erreur est survenue avec {User.name} : {e}")
    User.deconnection()
    print(f"Le client : {User.name} : s'est déconnecté")
    User.client.close()

ADRESSE = ''
PORT = 9999
serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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
        user = tab[i]
    print(f'Connexion de {adresseClient}, {retur}')
    thread = Thread(target=clientHandler(user))
    threads.append(thread)
    thread.start()
for i in threads:
    i.join()

for i in tab:
    tab.client.close()
    print('Fermeture de la connexion avec le client: ',+tab.name)
print('Arret du serveur.')
serveur.close()