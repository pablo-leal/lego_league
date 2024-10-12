import motor 
from hub import port, light_matrix
import math
import runloop
from time import sleep
#ROBOT MOVE FORWARD, LEFT
async def main():
    await move(73)
    await turn_left (335)
    await arm_move(195)

def cm_to_deg(cm):
    # One rotation= 27.6
    rotations = cm / 27.6
    # Return cm converted into degrees
    return math.floor(rotations * 360)

def wait_for_motor(degrees, speed):
    sleep(degrees/speed)
# MOVE ARM UP/DOWN
async def arm_move (degrees):
    motor.run_for_degrees (port.D, degrees, 200)

async def move (cm):
    degrees = cm_to_deg(cm)
    print("Moving forward " + str(cm) + " cm | " + str(degrees) + " degrees.");
    motor.run_for_degrees(port.A, -degrees, 720)
    motor.run_for_degrees(port.E, degrees, 720)
    wait_for_motor(degrees, 720)
# TURN LEFT
async def turn_left (degrees):
    motor.run_for_degrees(port.E, degrees, 720)
    wait_for_motor(degrees, 720)


runloop.run(main())