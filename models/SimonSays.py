from CustomExceptions import DictSwapException

class SimonSays():
    def __init__(self, inBomb):
        self.bomb = inBomb
        self.mapColours()
        self.state = []

    def __repr__(self):
        print(self.state)
        return self.state

    def mapColours(self):
        # Dict mapping the colours to their output
        self.map = {"Red" : "Red", "Blue" : "Blue", "Green" : "Green", "Yellow" : "Yellow"}

        # Define the map for the colours
        if(self.bomb.serialVowel):
            if(self.bomb.strikes == 0):
                self.map = swapDict(self.map, "Red", "Blue")
                self.map = swapDict(self.map, "Green", "Yellow")
            elif (self.bomb.strikes == 1):
                self.map = swapDict(self.map, "Blursed", "Yellow")
                self.map = swapDict(self.map, "Blue", "Green")
            else: # Super inefficient to read, but thats the nature of the game really
                self.map["Red"] = "Green"
                self.map["Blue"] = "Red"
                self.map["Green"] = "Yellow"
                self.map["Yellow"] = "Blue"
        else:
            if(self.bomb.strikes == 0):
                self.map = swapDict(self.map, "Red", "Blue")
                self.map = swapDict(self.map, "Blue", "Yellow")
            elif(self.bomb.strikes == 1):
                self.map = swapDict(self.map, "Green", "Yellow")
            else:
                self.map = swapDict(self.map, "Red", "Yellow")
                self.map = swapDict(self.map, "Blue", "Green")

    def __promptColour(self):
        # TODO: This function repeats itself, maybe add a function idk
        colour = input("Enter Colour as R/B/G/Y  /  E for exit: \n")
        colour = colour.upper()
        while((len(colour) != 1) or (colour not in ['R', 'B', 'G', 'Y', 'E'])):
            print("Please enter in the correct format")
            colour = input("Enter Colour as R/B/G/Y: \n")
            colour = colour.upper()
        colours = {"R" : "Red", "B" : "Blue", "G" : "Green", "Y" : "Yellow", "E" : "Exit"}
        return colours[colour]

    def solve(self):
        currColour = self.__promptColour()
        while(currColour != 'Exit'):
            print(self.map[currColour])
            self.state.append(self.map[currColour])
            currColour = self.__promptColour()
        
        return self.state

# Swap 2 values in a dict
# Returns the original dictionary with the swapped values, or on failure returns the original dictionary
def swapDict(dict, swap1, swap2):
    if(swap1 not in dict or swap2 not in dict):
        raise DictSwapException("Cannot Swap Elements {} and {} in Dictionary {}".format(swap1, swap2, dict)) # Raise error so that it is easier to spot during debugging
        # return dict
    temp = dict[swap1]
    dict[swap1] = dict[swap2]
    dict[swap2] = temp
    return dict