from Structures.action import Action
from drone import drone
# from time import sleep

def land():
    drone.land() if drone.is_flying == True else print("I have landed already!")
    
action = Action(land)