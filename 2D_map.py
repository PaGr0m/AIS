from RobotController import RobotController as robot
import time


def create2DMap(myRobot):
    STEP = 1

    time = 0
    list_2D_map = []
    dict_2D_map = {}

    for i in range(5):
        time.sleep(STEP)
        distance = str(myRobot.getIRDistance())

        time.sleep(STEP)
        myRobot.motorRun("left")

        time.sleep(STEP)
        myRobot.motorStop()

        time.sleep(STEP)

        time += STEP
        list_2D_map.append(str(time) + ":" + distance)
        dict_2D_map[str(time)] = distance

        print(list_2D_map)

    return list_2D_map


def findRobot(info):

    angle_time = 0
    min_distance = 10000

    for time, distance in info:
        if min_distance > distance:
            min_distance = distance
            angle_time = time

    return angle_time, min_distance


def main():
    myRobot = robot('/dev/ttyS1')
    time, distance = findRobot(create2DMap(myRobot))

if __name__ == "__main__":
    main()

