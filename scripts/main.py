from compute.clientTCP import ConnectToServer, sendString

if __name__ == '__main__':
    ConnectToServer()
    while 1:
        msg = input("Chaîne à envoyer au serveur : ")
        sendString(msg)
        if msg == "close":
            break
