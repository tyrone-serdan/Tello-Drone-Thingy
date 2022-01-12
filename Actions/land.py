from Structures.action import Action
from djitellopy import Tello as drone
# from time import sleep

def land():
    drone.land() if drone.is_flying == True else print("I have landed already!")
    
action = Action(land)