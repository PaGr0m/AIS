from Protocol import Protocol
from TcpClient import TcpClient
from  TcpServer import TcpServer

import time


def client_start():
    client = TcpClient()

    # TODO: Settings
    client.set_host("")
    client.set_port()
    client.connect()

    return client


def client_send(client):
    protocol = Protocol()

    # TODO: Setters
    protocol.set_ip("")
    protocol.set_color("")
    protocol.set_state("")
    protocol.set_message("")
    protocol.set_pos_x(float())
    protocol.set_pos_y(float())

    # Send protocol to robot (host, port)
    client.send(protocol.build_data())


def client_recieve(client):
    protocol = Protocol()
    protocol.save_data(client.receive())

    print(protocol)


def main():
    client = client_start()

    # To robot-server
    client_send(client)

    # From robot-server
    client_recieve(client)


if __name__ == "__main__":
    main()
