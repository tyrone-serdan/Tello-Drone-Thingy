from Structures.action import Action
from djitellopy import Tello as t
from time import sleep

def testFlight():
    t.takeoff()
    sleep(0.5)
    t.land()
    
action = Action(testFlight)