import socket

host = "192.168.3.50"
port = 445

client = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM)

client.connect((host, port))

test_list = "192.168.1.1" + ":" + "RED" + ":" + "msg" + ":" + "Hello"

client.send(test_list)
client.close()
