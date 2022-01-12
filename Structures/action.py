import typing_extensions


"""
Actions are a way to avoid adding if else statements for handling debugMode = on and debugMode = off on the drone.
"""
class Action:
    """
    Actions are a base class for functions for our Tello Drone.
    """
    def __init__(self, command) -> None:
        self.command = command
        self.name = command.__name__
    
    
    def debugStatement(self):
        """
        Prints out a statement saying function was successfully called instead of running code
        intended for the function. Useful for debugging.
        """
        commandName = self.name.capitalize()
        print(f"The function {commandName} has been successfully called.")
        
    