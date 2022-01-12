import importlib.util as iUtil
from djitellopy import Tello
from glob import glob
from time import sleep

drone = Tello()
actionsToLoad = glob('Actions/*.py')
actionsLoaded = dict()

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
        
        doAction(uInput, debug)

def connectDrone(mode: int):
    if (mode == 0):
        drone.connect()
    else:
        pass
        
    
def doAction(action: str, debugMode: int):
    if (debugMode == 0):
        actionsLoaded.get(action).command()
    else:
        actionsLoaded.get(action).debugStatement()

def loadActions():
    for actionPath in actionsToLoad:
        actionName = actionPath.replace("Actions" + '\\', "")
        actionKey = actionName.replace(".py", "")
        
        # Dynamically loads the Action module from the given path in actionsToLoad.
        spec = iUtil.spec_from_file_location(actionName, actionPath)
        action = iUtil.module_from_spec(spec)
        spec.loader.exec_module(action)
        
        # Allows us to call the Action safely
        actionsLoaded[actionKey] = action.action

    print(f"Loaded actions: {list(actionsLoaded.keys())}")
        


loadActions()
takeUserInput()