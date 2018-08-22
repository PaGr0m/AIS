import socket


class TcpClient(socket.socket):
    """
    TODO: Comments
    """

    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = ""
        self.port = None

    def set_host(self, host):
        self.host = host

    def set_port(self, port):
        self.port = port

    def connect(self):
        self.client.connect((self.host, self.port))

    def send(self, msg):
        self.client.send(msg.encode('utf-8'))

    def recieve(self):
        return self.client.recv(4096).decode('utf-8')
