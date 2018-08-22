from RobotController import RobotController as robot
import curses


def lifecycle(myRobot):
    printMainMenu()
    userInput = raw_input('>> ')
    userInput = userInput.split(' ')
    command = int(userInput[0])

    if command == 1:
        print myRobot.check()
    elif command == 2:
        print myRobot.getVoltage()
    elif command == 3:
        print myRobot.getIRDistance()
    elif command == 4:
        myRobot.beep(int(userInput[1]), int(userInput[2]))
    elif command == 5:
        myRobot.setLed(True, int(userInput[1]), int(userInput[2]), int(userInput[3]))
    elif command == 6:
        myRobot.setLed(False)
    elif command == 7:
        myRobot.softLedBlink(int(userInput[1]), int(userInput[2]), int(userInput[3]), int(userInput[4]),
                             int(userInput[5]))
    elif command == 8:
        callMotorSteering()
    else:
        print '[ERROR]: typo error'


def callMotorSteering():
    stdscr = curses.initscr()
    stdscr.keypad(1)
    stdscr.addstr(0, 0, "Motor steering enabled. Press \'q\' to exit. Use arrows, space.")
    stdscr.refresh()

    key = ''
    prevKey = '1'
    while key != ord('q'):
        key = stdscr.getch()
        # stdscr.addch(2,10,key)
        stdscr.refresh()
        if key == prevKey:
            pass
        if key == curses.KEY_UP:
            myRobot.motorRun('forward')
        elif key == curses.KEY_DOWN:
            myRobot.motorRun('backward')
        elif key == curses.KEY_LEFT:
            myRobot.motorRun('left')
        elif key == curses.KEY_RIGHT:
            myRobot.motorRun('right')
        elif str(key) == '339':  # pg up left ellyptic
            myRobot.motorRun('left_elyptic')
        elif str(key) == '338':  # pg down right ellyptic
            myRobot.motorRun('right_elyptic')
        elif str(key) == '32':
            myRobot.motorStop()
        prevKey = key
    curses.endwin()


def printMainMenu():
    print '      -=Control panel=-'
    print '1) Check if STM32 is alive'
    print '2) STM32 voltage'
    print '3) Current IR distance'
    print '4) Beep args: (num, time)'
    print '5) LED ON args: (R, G, B)'
    print '6) LED OFF'
    print '7) LED soft blink args: (R, G, B, n, t)'
    print '8) Motor menu'


if __name__ == '__main__':
    myRobot = robot('/dev/ttyS1')
    while True:
        lifecycle(myRobot)
