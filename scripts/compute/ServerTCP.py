import socket
ADRESSE = ''
PORT = 4258

serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serveur.bind((ADRESSE, PORT))
serveur.listen(1)
client, adresseClient = serveur.accept()
print('Connexion de ', adresseClient)
data = ""
while data != 'close':
    data = client.recv(1024)
    data = data.decode()
    if data:
        print(data)

print('Fermeture de la connexion avec le client.')
client.close()
print('Arret du serveur.')
serveur.close()