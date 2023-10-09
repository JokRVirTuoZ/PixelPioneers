class User:
    def __init__(self, client, address, id):
        self.client = client
        self.ip = address[0]
        self.port = address[1]
        self.id = id
        self.isConnected = False
        self.connection()
        self.name = ""

    def connection(self):
        #compute
        self.isConnected = True

    def deconnection(self):
        #compute
        self.isConnected = False

    def setName(self, name):
        self.name = str(name)

