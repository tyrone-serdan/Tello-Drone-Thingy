from Structures.action import Action
from djitellopy import Tello as drone
# from time import sleep

def takeOff():
    drone.takeoff() if drone.is_flying == False else print("I am flying already!")
    
action = Action(takeOff)