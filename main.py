class SimonSays():
    def __init__(self, inBomb):
        bomb = inBomb

    def __repr__(self):
        pass

    # Dict mapping the colours to their output
    map = {}
    def solve(self):
        colours = [input("Please Enter the First Colour: \n")]


class Bomb():
    def __init__(self):
        strikes = 0
        parallel = __setParallel()

    def __setParallel(self):
        def __getUserIn(): # Get the user input and convert it to upper case
            userIn = input("Does the bomb have a parallel port? Y/N") # Get the user input
            userIn = userIn.upper()
            return userIn
        
        userIn = __getUserIn()
        while(len(userIn) < 1 && (userIn[0] != "Y" || userIn[0] != "N")):
            print("Please enter Y/N")
            userIn = __getUserIn()
        
        if (userIn[0] == "Y"):
            return True
        else:
            return False    

        