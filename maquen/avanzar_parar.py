# Imports go at the top
from microbit import *
from maqueen import *

robot = Maqueen()
robot.forward()
sleep(1000)
robot.motor_stop_all()
