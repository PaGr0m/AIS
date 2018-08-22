from RobotController import RobotController as robot
import curses
import time

myRobot = robot('/dev/ttyS1')

while True:
    # myRobot.beep(int(4), int(4))
    # myRobot.motorRun('forward')
    myRobot.setLed(True, int(0), int(255), int(0))
    time.sleep(1)
    myRobot.setLed(False)
    time.sleep(1)

    dis = 0

    myRobot.motorRun('forward')
    time.sleep(0.1)

    while dis < 2000:
        dis = myRobot.getIRDistance()
        print(dis)
        time.sleep(0.1)

    myRobot.motorStop()
    time.sleep(2)

    myRobot.motorRun('backward')

    time.sleep(1)

    myRobot.motorStop()

    time.sleep(1)

# for number in range(8):
# 	myRobot.motorRun('forward')
# 	time.sleep(1.45/8)
# 	myRobot.motorStop()
# 	time.sleep(0.5)
# print myRobot.getIRDistance()
# time.sleep(1)
