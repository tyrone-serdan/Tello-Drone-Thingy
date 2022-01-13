from Structures.action import Action
from drone import drone
from time import sleep

def testFlight():
    drone.takeoff()
    sleep(0.5)
    drone.land()
    
action = Action(testFlight)