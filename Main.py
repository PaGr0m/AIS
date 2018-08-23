from Protocol import Protocol
from TcpClient import TcpClient
from TcpServer import TcpServer
from RobotController import RobotController
from getkey import getkey, keys

import time
import socket
import os


def client_start():
    client = TcpClient()

    # TODO: Settings
    client.set_host("192.168.3.50")
    client.set_port(445)
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


def main_menu():
    print("\n+---------- MENU ----------+")
    print("| 1. Set up connection     |")
    print("| 2. Send a message        |")
    print("| 3. Receive a message     |")
    print("| 4. Beep                  |")
    print("| 5. Run forward           |")
    print("| 6. Show distance         |")
    print("| 7. Set LED               |")
    print("| 8. Soft Blink            |")
    print("| 9. Stop motor            |")
    print("| 0. Exit                  |")
    print("+--------------------------+\n")


def main():
    robot = RobotController("/dev/ttyS1")
    os.system("clear")

    while True:

        main_menu()
        answer = raw_input("Enter the command --> ")
        os.system("clear")

        if answer == "1":
            """ Connection """
            try:
                client = client_start()
                print("[DEBUG] >> Connected")
            except:
                print("[DEBUG] >> Connection Error")

        elif answer == "2":
            """ Send <MESSAGE> """
            try:
                client.send("READY")
                print("[DEBUG] >> Message is sended")
            except:
                print("[DEBUG] >> Send Error")

        elif answer == "3":
            """ Receive <MESSAGE> """
            data = client.recieve()
            print("[DEBUG] >> From JP: ", data)

            if data == "START":
                # 1 time = 100 ms
                robot.beep(1, 2)

        elif answer == "4":
            """ Beep """
            robot.beep(1, 2)

        elif answer == "5":
            """ Run robot """
            # robot.motorRun("forward", 2)
            # robot.motorStop()
            robot.motor.forward()
            # robot.motor.stop()

        elif answer == "6":
            """ Show distance """
            distance = robot.ir.get_distance()
            print("[DEBUG] >> ", distance)

        elif answer == "7":
            """ Set LED """
            red = int(raw_input("Input RED color --> "))
            green = int(raw_input("Input GREEN color --> "))
            blue = int(raw_input("Input BLUE color --> "))
            robot.led.set(True, red, green, blue)
            print("[DEBUG] >> LED is installed")

        elif answer == "8":
            """ Soft Blink"""
            red = int(raw_input("Input RED color --> "))
            green = int(raw_input("Input GREEN color --> "))
            blue = int(raw_input("Input BLUE color --> "))
            number = int(raw_input("Input NUMBER color --> "))
            duration = int(raw_input("Input DURATION color --> "))
            robot.led.soft_blink(red, green, blue, number, duration)

        elif answer == "9":
            robot.motor.stop()

        elif answer == "*":
            """ Hands control """
            while True:
                key = getkey()
                if key == keys.UP:
                	robot.motor.forward(1)
                	print 'up'
                elif key == keys.DOWN:
                    robot.motor.backward(1)
                    print 'down'
                elif key == keys.LEFT:
                    robot.motor.left(1)
                    print 'left'
                elif key == keys.RIGHT:
                    robot.motor.right(1)
                    print 'right'
                else:
                	robot.motor.stop()

        elif answer == "0":
            break


    # TODO: later
    # To robot-server
    # client_send(client)

    # From robot-server
    # client_recieve(client)

    print("End")


if __name__ == "__main__":
    main()
