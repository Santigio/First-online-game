import socket

"""In other to connect multiple clients to our server, we need a network that will keep sending and receiving 
objects like for instance when we move a object over one screen, it should update over the other 
client's screen. That's what network class helps us with."""
class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.1.73"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.pos = self.connect()

    def getPos(self):
        return self.pos

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass
    """Also for security reason, we are encoding and decoding information, and our try and accept 
    block also ignores whenever client decided disconnect. 
    Now this is important to prevent falling into infinite loop"""
    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)