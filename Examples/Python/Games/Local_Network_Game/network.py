import socket
import sys


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "10.56.64.165"
        self.port = 5555
        self.address = (self.server, self.port)
        self.pos = self.connect()

    def get_pos(self):
        return self.pos

    def connect(self):
        try:
            self.client.connect(self.address)
            return self.client.recv(2048).decode()
        except:
            e = sys.exc_info()[0]
            print(e)
            print("Error with network connection...")

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)
