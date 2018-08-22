REQUEST = {
'CHECK'          : bytearray.fromhex('10 00 00 10'),
'GET_VOLTAGE'    : bytearray.fromhex('12 05 00 20'),
'GET_IR_DISTANCE': bytearray.fromhex('14 07 00 20')
}

RESPONSE = {
'CHECK'          : bytearray.fromhex('20 00 00 10 01'),
'VOLTAGE'        : bytearray.fromhex('20 05 00 20 00 00'),
'DISTANCE'       : bytearray.fromhex('20 07 00 20 00 00')
}

COMMAND = {
'BEEP'           : bytearray.fromhex('03 06 21 00 00 00'),
'LED_OFF'        : bytearray.fromhex('01 02 00 00'),
'LED_ON'         : bytearray.fromhex('01 01 31 00 00 00 00'),
'LED_SOFT_BLINK' : bytearray.fromhex('01 04 51 00 00 00 00 00 00')
}

MOTOR = {
'FWARD_T'        : bytearray.fromhex('05 08 11 00 00'),
'BWARD_T'        : bytearray.fromhex('05 09 11 00 00'),
'LTURN_T'        : bytearray.fromhex('05 0B 11 00 00'),
'RTURN_T'        : bytearray.fromhex('05 0A 11 00 00'),

'FWARD'          : bytearray.fromhex('05 0D 00 00'),
'BWARD'          : bytearray.fromhex('05 0E 00 00'),
'LTURN'          : bytearray.fromhex('05 10 00 00'),
'RTURN'          : bytearray.fromhex('05 0F 00 00'),
'STOP'           : bytearray.fromhex('05 0C 00 00'),

'LEFT_ELYPTIC'   : bytearray.fromhex('05 11 00 00'),
'RIGHT_ELYPTIC'  : bytearray.fromhex('05 12 00 00')
}
