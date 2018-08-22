import serial
from HexMaestro import HexMaestro as maestro


class UARTMan:
    def __init__(self, uartName):
        self.__name = uartName
        self.__receiveBuffer = b''

    def open(self):
        self.__serial = serial.Serial(self.__name, 115200, timeout=0.25)

    def send(self, hexByteString):
        # print hexByteString
        self.__serial.write(hexByteString)

    def receive(self):
        command = self.__serial.read(4)
        args = b''
        command = maestro(command)
        bytesToReceive = command.getArgsToReceive()
        command = command.getPackedByteString()
        for i in range(0, bytesToReceive, 1):
            command.append(self.__serial.read(1))
        return command

    def close(self):
        self.__serial.close()
