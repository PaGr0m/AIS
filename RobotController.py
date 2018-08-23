from HexMaestro import HexMaestro as maestro
from UARTMan import UARTMan as uart

import Constants as CONST


class RobotController:
    def __init__(self, name):
        self.__UARTConnection = uart(name)
        self.__UARTConnection.open()

        self.motor = self.Motor(name)
        self.ir = self.IR(name)
        self.led = self.LED(name)

    def __del__(self):
        self.__UARTConnection.close()

    def motorRun(self, direction='forward', time=0):
        if time == 0:
            if direction == 'forward':
                req = CONST.MOTOR['FWARD']
            elif direction == 'backward':
                req = CONST.MOTOR['BWARD']
            elif direction == 'left':
                req = CONST.MOTOR['LTURN']
            elif direction == 'right':
                req = CONST.MOTOR['RTURN']
            elif direction == 'right_elyptic':
                req = CONST.MOTOR['RIGHT_ELYPTIC']
            elif direction == 'left_elyptic':
                req = CONST.MOTOR['LEFT_ELYPTIC']
        else:
            if direction == 'forward':
                req = CONST.MOTOR['FWARD_T']
            elif direction == 'backward':
                req = CONST.MOTOR['BWARD_T']
            elif direction == 'left':
                req = CONST.MOTOR['LTURN_T']
            elif direction == 'right':
                req = CONST.MOTOR['RTURN_T']
            req = maestro(req)
            req.setArg('int', 0, time)
            req = req.getPackedByteString()
        self.__UARTConnection.send(req)

    def motorStop(self):
        req = CONST.MOTOR['STOP']
        # print req
        self.__UARTConnection.send(req)

    def check(self):
        req = CONST.REQUEST['CHECK']
        self.__UARTConnection.send(req)
        receive = self.__UARTConnection.receive()
        receive = maestro(receive)
        byte0 = receive.getArg('int', 0)
        return '%d' % (byte0)

    def getVoltage(self):  # to be realized
        req = CONST.REQUEST['GET_VOLTAGE']
        self.__UARTConnection.send(req)
        receive = self.__UARTConnection.receive()
        receive = maestro(receive)
        byte0 = receive.getArg('int', 0)
        byte1 = receive.getArg('int', 1)
        voltage = byte0 * 255 + byte1
        return 'Voltage: %f' % (voltage)

    def getIRDistance(self):
        req = CONST.REQUEST['GET_IR_DISTANCE']
        self.__UARTConnection.send(req)
        receive = self.__UARTConnection.receive()
        receive = maestro(receive)
        byte0 = receive.getArg('int', 0)
        byte1 = receive.getArg('int', 1)
        distance = byte0 * 255 + byte1
        return distance

    # return 'Distance: %f'%(distance)

    def getUSDistance(self):
        pass  # returns ultrasonic distance (front)

    def beep(self, number=1, duration=1):
        req = CONST.COMMAND['BEEP']
        req = maestro(req)
        req.setArg('int', 0, number)
        req.setArg('int', 1, duration)
        req = req.getPackedByteString()
        self.__UARTConnection.send(req)

    def setLed(self, status=True, red=0, green=255, blue=0):
        if status:
            req = CONST.COMMAND['LED_ON']
            req = maestro(req)
            req.setArg('int', 2, red)  #
            req.setArg('int', 1, green)
            req.setArg('int', 0, blue)  #
            req = req.getPackedByteString()
        elif not status:
            req = CONST.COMMAND['LED_OFF']
        self.__UARTConnection.send(req)

    def softLedBlink(self, red=0, green=255, blue=0, number=2, duration=10):
        req = CONST.COMMAND['LED_SOFT_BLINK']
        req = maestro(req)
        req.setArg('int', 2, red)  #
        req.setArg('int', 1, green)
        req.setArg('int', 0, blue)  #
        req.setArg('int', 3, number)
        req.setArg('int', 4, duration)
        req = req.getPackedByteString()
        self.__UARTConnection.send(req)

    # -----------------------------------------------------

    class Motor:
        def __init__(self, name):
            self.req = ""
            self.__UARTConnection = uart(name)
            self.__UARTConnection.open()

        #
        # def run(self):
        #     self.__UARTConnection.send(self.req)

        def forward(self, time=0):
            if time == 0:
                req = CONST.MOTOR['FWARD']
            else:
                req = CONST.MOTOR['FWARD_T']

                req = maestro(req)
                req.setArg('int', 0, time)
                req = req.getPackedByteString()
            self.__UARTConnection.send(req)

        def backward(self, time=0):
            if time == 0:
                req = CONST.MOTOR['BWARD']
            else:
                req = CONST.MOTOR['BWARD_T']

                req = maestro(req)
                req.setArg('int', 0, time)
                req = req.getPackedByteString()
            self.__UARTConnection.send(req)

        def left(self, time=0):
            if time == 0:
                req = CONST.MOTOR['LTURN']
            else:
                req = CONST.MOTOR['LTURN_T']

                req = maestro(req)
                req.setArg('int', 0, time)
                req = req.getPackedByteString()
            self.__UARTConnection.send(req)

        def right(self, time=0):
            if time == 0:
                req = CONST.MOTOR['RTURN']
            else:
                req = CONST.MOTOR['RTURN_T']

                req = maestro(req)
                req.setArg('int', 0, time)
                req = req.getPackedByteString()
            self.__UARTConnection.send(req)

        def left_elyptic(self):
            req = CONST.MOTOR['RIGHT_ELYPTIC']
            self.__UARTConnection.send(req)

        def right_elyptic(self):
            req = CONST.MOTOR['LEFT_ELYPTIC']
            self.__UARTConnection.send(req)

        def stop(self):
            req = CONST.MOTOR['STOP']
            self.__UARTConnection.send(req)

    class IR:
        def __init__(self, name):
            self.req = ""
            self.__UARTConnection = uart(name)
            self.__UARTConnection.open()

        def get_distance(self):
            req = CONST.REQUEST['GET_IR_DISTANCE']
            self.__UARTConnection.send(req)
            receive = self.__UARTConnection.receive()
            receive = maestro(receive)
            byte0 = receive.getArg('int', 0)
            byte1 = receive.getArg('int', 1)
            distance = byte0 * 255 + byte1

            return distance

    class LED:
        def __init__(self, name):
            self.req = ""
            self.__UARTConnection = uart(name)
            self.__UARTConnection.open()

        def set(self, status=True, red=0, green=255, blue=0):
            if status:
                req = CONST.COMMAND['LED_ON']
                req = maestro(req)
                req.setArg('int', 2, red)  #
                req.setArg('int', 1, green)
                req.setArg('int', 0, blue)  #
                req = req.getPackedByteString()
            elif not status:
                req = CONST.COMMAND['LED_OFF']
            self.__UARTConnection.send(req)

        def soft_blink(self, red=0, green=255, blue=0, number=2, duration=10):
            req = CONST.COMMAND['LED_SOFT_BLINK']
            req = maestro(req)
            req.setArg('int', 2, red)  #
            req.setArg('int', 1, green)
            req.setArg('int', 0, blue)  #
            req.setArg('int', 3, number)
            req.setArg('int', 4, duration)
            req = req.getPackedByteString()
            self.__UARTConnection.send(req)
