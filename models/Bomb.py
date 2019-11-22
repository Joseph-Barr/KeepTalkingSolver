class Bomb():
    def __init__(self):
        self.strikes = 0
        self.parallel = self.setParallel()
        self.serialVowel = False
        self.lastSerialDigit = 0

    # Ask the user whether the bomb has a parallel port
    def setParallel(self):
        def __getUserIn(): # Get the user input and convert it to upper case
            userIn = input("Does the bomb have a parallel port? Y/N\n") # Get the user input
            userIn = userIn.upper()
            return userIn
        
        userIn = __getUserIn()
        while((len(userIn) != 1) or (userIn[0] != "Y" and userIn[0] != "N")):
            print("Please enter Y/N")
            userIn = __getUserIn()
        
        if (userIn[0] == "Y"):
            return True
        else:
            return False    
