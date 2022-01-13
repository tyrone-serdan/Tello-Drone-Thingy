import importlib.util as iUtil
from djitellopy import Tello
from glob import glob
from time import sleep

drone = Tello()
actionsLoaded = dict()
activeActions = list()

def takeUserInput():
    uInput = input("Type y to activate debug mode, n if not needed. ")
    debug = 1 if uInput.lower() == "y" else 0
    connectDrone(debug)
    
    while True:
        uInput = input("Input action for Tello Drone. \n")
        
        if (uInput.lower() == "exit"):
            if (drone.is_flying == True):
                drone.land()
            quit()
        elif (uInput.lower() == "list"):
            print(activeActions)
            pass
            
        doAction(uInput, debug)

def connectDrone(mode: int):
    if (mode == 0):
        drone.connect()
    else:
        pass
        
    
def doAction(actionSelected: str, debugMode: int):
    foundAction = actionSelected in activeActions
    
    if (foundAction == False):
        return
    
    if (debugMode == 0 and foundAction == True):
        actionsLoaded.get(actionSelected).command()
    else:
        actionsLoaded.get(actionSelected).debugStatement()

def loadActions():
    actionsToLoad = glob('Actions/*.py')
    
    for actionPath in actionsToLoad:
        actionName = actionPath.replace("Actions" + '\\', "")
        actionKey = actionName.replace(".py", "")
        
        # Dynamically loads the Action module from the given path in actionsToLoad.
        spec = iUtil.spec_from_file_location(actionName, actionPath)
        action = iUtil.module_from_spec(spec)
        spec.loader.exec_module(action)
        
        # This is to have a list ready for the user to see the available actions for our Drone.
        activeActions.append(actionKey)
        
        # Allows us to call the Action safely
        actionsLoaded[actionKey] = action.action


loadActions()
takeUserInput()