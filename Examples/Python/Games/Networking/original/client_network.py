import selectors
import socket

import libclient


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sel = selectors.DefaultSelector()
        self.host = "192.168.1.239"
        self.port = 65432
        self.action = "start"
        self.value = "position"
        self.request = self.create_request()        
        self.position = self.start_connection(self.host, self.port, self.request, self.sel)

    def create_request(self):
        if self.action == "start":
            return dict(
                type="text/json",
                encoding="utf-8",
                content=dict(action=self.action, value=self.value),
            )
        else:
            return dict(
                type="binary/custom-client-binary-type",
                encoding="binary",
                content=bytes(self.action + self.value, encoding="utf-8"),
            )

    def start_connection(self):
        addr = (self.host, self.port)
        print("starting connection to", addr)
        self.client.setblocking(False)
        self.client.connect_ex(addr)
        events = selectors.EVENT_READ | selectors.EVENT_WRITE
        message = libclient.Message(self.sel, self.client, addr, self.request)
        self.sel.register(self.client, events, data=message)
