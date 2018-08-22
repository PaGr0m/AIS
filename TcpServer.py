import socket
import threading


class TcpServer(socket.socket, threading.Thread):
    """
    TODO: Comments
    """

    def __init__(self):
        self.__host = ""
        self.__port = None
        self.__serversock = None
        self.__maxClients = 0
        self.__recievedMsg = []
        self.__clientSock = []
        self.__serverThread = None

    # Thread
    def __server(self):
        for i in range(self.__maxClients):
            self.__clientSock.append(self.__serversock.accept())
            print(self.__clientSock[i][1])

    # Thread
    def __recieve(self):
        while True:
            for e in self.__clientSock:
                rcvmsg = e[0].recv(4096)
                self.__recievedMsg.append(rcvmsg.decode('utf-8'))

    def set_server(self, host, port, max_clients):
        self.__host = host
        self.__port = port
        self.__maxClients = max_clients

    def send_all(self, msg):
        for client_socket, _ in self.__clientSock:
            client_socket.sendall(msg.encode('utf-8'))

    def get_msg(self):
        if len(self.__recievedMsg) != 0:
            msg = self.__recievedMsg[0]
            self.__recievedMsg.pop(0)
            return True, msg
        else:
            return False, ''

    def start_server(self):
        self.__serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__serversock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.__serversock.bind((self.__host,self.__port))
        self.__serversock.listen(10)

        self.__serverThread = threading.Thread(target=self.__server, name="server", args=())
        self.__serverThread.setDaemon(True)
        self.__serverThread.start()

        self.__recieveThread = threading.Thread(target=self.__recieve, name="recieve", args=())
        self.__recieveThread.setDaemon(True)
        self.__recieveThread.start()
