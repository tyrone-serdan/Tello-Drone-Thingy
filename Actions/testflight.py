from Structures.action import Action
from djitellopy import Tello as drone
from time import sleep

def testFlight():
    drone.takeoff()
    sleep(0.5)
    drone.land()
    
action = Action(testFlight)