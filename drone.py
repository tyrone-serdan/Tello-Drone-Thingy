from logging import debug
from djitellopy import Tello
from glob import glob
import importlib.util as iUtil

drone = Tello()
actionsToLoad = glob('Actions/*.py')
actionsLoaded = dict()

def takeUserInput():
    uInput = input("Type y to activate debug mode, n if not needed. ")
    debug = 1 if uInput.lower() == "y" else 0
    
    while True:
        uInput = input("Input action for tello drone. ")
        
        if (uInput.lower() == "exit"):
            quit()
        
        doAction(uInput, debug)
    
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
        


loadActions()
takeUserInput()