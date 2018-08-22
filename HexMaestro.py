class HexMaestro:

    def __init__(self, rawHex):
        self.__rawByteStringHex = rawHex
        self.__commandTouple = self.__splitUnpacked('command')
        self.__argsTouple = self.__splitUnpacked('args')

    def __splitUnpacked(self, part):
        if part == 'command':
            unpacked = self.__unpackFromByteHex(self.__rawByteStringHex[:4])
        elif part == 'args':
            unpacked = self.__unpackFromByteHex(self.__rawByteStringHex[4:])
        return [unpacked[i:i + 2] for i in range(0, len(unpacked), 2)]  # return ['01', '20', 'bb', '0a']

    def __unpackFromByteHex(self, string):
        unpacked = bytes(string)
        unpacked = unpacked.encode('hex')
        return unpacked  # return '0120bb0a'

    def __fillByte(self, value):
        if len(value) < 2:
            return '0' + value
        else:
            return value

    def getArg(self, coding, number):
        if coding == 'hex':
            return self.__argsTouple[number]
        elif coding == 'int':
            return int(self.__argsTouple[number], 16)

    def getArgsTouple(self):
        return self.__argsTouple

    def getArgsToupleSize(self):
        return len(self.__argsTouple)

    def getArgsToReceive(self):
        return int(self.__commandTouple[3][0], 16)

    def getCommandTouple(self):
        return self.__commandTouple

    def getByte(self, coding, number):
        if coding == 'hex':
            return self.__commandTouple[number]  # return '01'
        elif coding == 'int':
            return int(self.__commandTouple[number], 16)  # return '255' of 'ff'

    def getPackedByteString(self):
        glueReq = ''
        for i in self.__commandTouple:
            glueReq += i
        for i in self.__argsTouple:
            glueReq += i
        return bytearray.fromhex(glueReq)

    def setArg(self, coding, number, value):
        if coding == 'hex':
            self.__argsTouple[number] = self.__fillByte(value)
        elif coding == 'int':
            self.__argsTouple[number] = self.__fillByte(hex(value)[2:])

    def setByte(self, coding, number, value):
        if coding == 'hex':
            self.__commandTouple[number] = self.__fillByte(value)
        elif coding == 'int':
            self.__commandTouple[number] = self.__fillByte(hex(value)[2:])
