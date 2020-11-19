import time
import serial
from math import pi
import numpy
import socket
import sys

import waypoints as wp
import kg_robot as kgr

#task = "Potato Stab"
#task = "Potato Smash"
#task = "Blank"
#task = "Get J"
#task = "TestForceMove"
#task = "Potato Stab Slowly"
task = "Potato Stab Slowly Operator Start"


def main():
    print("------------Configuring Burt-------------\r\n")
    robot = kgr.kg_robot(port=30010,db_host="169.254.250.80")
    #burt = kgr.kg_robot(port=30010,ee_port="COM32",db_host="192.168.1.51")
    print("----------------Hi Burt!-----------------\r\n\r\n")

    ###Change the output name inside this script !!!!!!!!!!!!!!!!!
    ##exec(open("USBread/USBread.py").read())


    if task == "Potato Stab Slowly":
        print("Task: Potato Stab Slowly")
        #Moving home
        robot.home()
        time.sleep(1)

        #moving to stab 1 position (just above potato)
        robot.translatel_rel([-0.012, -0.012, -0.0772])   #ITS IN METERS - REMEMBER !!!!!!!!!!!!!!    # translation to make this stab most on the left aded
        time.sleep(1)
        #sys.exit()
        #stab 1
        for i in range(16):
            robot.translatel_rel([-0, -0, -0.0015])
            time.sleep(1)
        robot.translatel_rel([-0, -0, 0.0015*16])
        time.sleep(1)

        for i in range(6):
            # moving to stab 2 position (just above potato)
            robot.translatel_rel([0.004, 0.004, 0])
            time.sleep(3)
            # stab 2
            for i in range(16):
                robot.translatel_rel([-0, -0, -0.0015])
                time.sleep(1)
            # un-stab2
            robot.translatel_rel([-0, -0, 0.0015*16])
            time.sleep(1)

        robot.home()
        time.sleep(1)




    if task == "Potato Stab":
        print("Potato stab task ON")
        #Moving home
        robot.home()
        time.sleep(1)

        #moving to stab 1 position (just above potato)
        robot.translatel_rel([-0.012, -0.012, -0.0772])   #ITS IN METERS - REMEMBER !!!!!!!!!!!!!!    # translation to make this stab most on the left aded
        time.sleep(1)
        #stab 1
        robot.translatel_rel([0, 0, -0.0385])
        time.sleep(1)
        # un - stab 1
        robot.translatel_rel([0, 0, 0.0385])
        time.sleep(1)

        # moving to stab 2 position (just above potato)
        robot.translatel_rel([0.004, 0.004, 0])
        time.sleep(1)
        # stab 2
        robot.translatel_rel([0, 0, -0.0385])
        time.sleep(1)
        # un - stab 2
        robot.translatel_rel([0, 0, 0.0385])
        time.sleep(1)

        # moving to stab 3 position (just above potato)
        robot.translatel_rel([0.004, 0.004, 0])
        time.sleep(1)
        # stab 3
        robot.translatel_rel([0, 0, -0.0385])
        time.sleep(1)
        # un - stab 3
        robot.translatel_rel([0, 0, 0.0385])
        time.sleep(1)

        # moving to stab 4 position (just above potato)
        robot.translatel_rel([0.004, 0.004, 0])
        time.sleep(1)
        # stab 4
        robot.translatel_rel([0, 0, -0.0385])
        time.sleep(1)
        # un - stab 4
        robot.translatel_rel([0, 0, 0.0385])
        time.sleep(1)

        # moving to stab 5 position (just above potato)
        robot.translatel_rel([0.004, 0.004, 0])
        time.sleep(1)
        # stab 5
        robot.translatel_rel([0, 0, -0.0385])
        time.sleep(1)
        # un - stab 5
        robot.translatel_rel([0, 0, 0.0385])
        time.sleep(1)

        # moving to stab 6 position (just above potato)
        robot.translatel_rel([0.004, 0.004, 0])
        time.sleep(1)
        # stab 6
        robot.translatel_rel([0, 0, -0.0385])
        time.sleep(1)
        # un - stab 6
        robot.translatel_rel([0, 0, 0.0385])
        time.sleep(1)

        # moving to stab 7 position (just above potato)
        robot.translatel_rel([0.004, 0.004, 0])
        time.sleep(1)
        # stab 7
        robot.translatel_rel([0, 0, -0.0385])
        time.sleep(1)
        # un - stab 7
        robot.translatel_rel([0, 0, 0.0385])
        time.sleep(1)


        # Go home after finished work
        robot.home()
        time.sleep(1)

    if task == "Potato Smash":
        print("Potato Smash Task ON")


#        robot.movej([-1.8207, -1.60221225, -1.70344, 0.041538, 1.86069, 0.104196])
#        print(robot.getj())
#        time.sleep(1)
#        robot.translatel_rel([0, 0, -0.05])
#        time.sleep(1)
#        robot.movej([-1.8207, -1.60221225, -1.70344, 0.041538, 1.86069, 0.104196])

        ####robot homeing itself automatically, so move the tool to horizontal
        robot.movej([-1.8207, -1.60221225, -1.70344, 0.041538, 1.86069, 0.104196])
        time.sleep(1)
        ####move arm to the right side
        robot.movej([0.900374, -1.99436, -1.30906, 0.171454, 1.58095, -0.0251206])
        time.sleep(1)
        ####rotate tool for smashing
        robot.movej([0.900398, -1.99436, -1.30914, 0.17143, 1.58092, 1.16401])
 #       robot.movej([0.900422, -1.99437, -1.30912, 0.171442, 1.58091, 2.86051])     ####position for cutting
        time.sleep(1)

        sys.exit()

        #####Replace this with smashing with force i guess
        robot.translatel_rel([0, 0, -0.05])
        time.sleep(1)
        robot.translatel_rel([0, 0, 0.05])
        time.sleep(1)

        ####go back to the left side
        robot.movej([-1.8207, -1.60221225, -1.70344, 0.041538, 1.86069, 0.104196])
        time.sleep(1)
        #home the robot
        robot.home()

    if task == "Get J":
        print(robot.getj())


    if task == "TestForceMove":
        print("Task: TestForceMove")
        robot.force_move([0,0,-1], force = 30)

    if task == "Potato Stab Slowly Operator Start":
        print("The task is: Potato Stab Slowly Operator Start")
        #robot.speedl([0.1,0.1,0.1,0.1,0.1,0.1],0.01,10,False)
        for i in range(16):
            robot.translatel_rel([-0, -0, -0.0015])
            time.sleep(2)



if __name__ == '__main__': main()
