from djitellopy import Tello
from glob import glob
import importlib.util as iUtil

# drone = Tello()
debugMode = 0

actionsToLoad = glob('Actions/*.py')
actionsLoaded = dict()

for actionPath in actionsToLoad:
    actionName = actionPath.replace("Actions" + '\\', "")
    actionKey = actionName.replace(".py", "")
    
    # Dynamically loads the Action module from the given path in actionsToLoad.
    spec = iUtil.spec_from_file_location(actionName, actionPath)
    action = iUtil.module_from_spec(spec)
    spec.loader.exec_module(action)
    
    # Allows us to call the Action safely
    actionsLoaded[actionKey] = action.action
    
actionsLoaded.get("initialize").command()