from General import getLetterArrayIn

class SimpleWires():
    def __init__(self, bomb):
        self.bomb = bomb

    def __repr__(self):
        return self.wires

    def __str__(self):
        pass

    def getSequence(self):
        self.wires = getLetterArrayIn(0, "rywblk")
        self.wires = self.splitSimpleWires(self.wires)

    # Splits a set of valid characters into an array of simple wires
    def splitSimpleWires(self, validCharacters):
        validWires = ['r', 'y', 'w', 'bl', 'bk']
        output = []

        for pos, char in enumerate(validCharacters):
            if(char == 'b'):
                if((char + validCharacters[pos + 1]) in validWires):
                    output.append(char + validCharacters[pos + 1])
            elif(char in validWires):
                output.append(char)
        return output
    
    # Solves for self.wires
    # Returns the position of the wire to cut as both a string and a integer eg ("Last", 3)
    def solve(self):
        # Implement the long list of rules for simple wires
        if(self.wires.length == 3):
            if("r" not in self.wires):
                return "Second", 2
            elif(self.wires[-1] == 'w'):
                return "Last", self.wires.length
            elif(self.wires.count('bl') > 1):
                return "Last Blue", self.wires.rfind('b') + 1
            else:
                return "Last", self.wires.length

        elif(self.wires.length == 4):
            if(self.wires.count('r') > 1 and self.bomb.lastSerialDigit % 2 != 0):
                return "Last Red", self.wires.rfind('r')
            elif(self.wires[-1] == 'y' and self.wires.count('r') == 0):
                return "First", 1
            elif(self.wires.count('bl') == 1):
                return "First", 1
            elif(self.wires.count('y') > 1):
                return "Last", self.wires.length
            else:
                return "Second", 2

        elif(self.wires.length == 5):
            if(self.wires[-1] == 'bk' and self.bomb.lastSerialDigit % 2 != 0):
                return "Fourth", 4
            elif(self.wires.count('r') == 1 and self.wires.count('y') > 1):
                return "First", 1
            elif(self.wires.count('bk') == 0):
                return "Second", 2
            else:
                return "First", 1

        elif(self.wires.length == 6):
            if(self.wires.count('y') == 0 and self.bomb.lastSerialDigit % 2 != 0):
                return "Third", 3
            elif(self.wires.count('y') == 1 and self.wires.count('w') > 1):
                return "Fourth", 4
            elif(self.wires.count('r') == 0):
                return "Last", self.wires.length
            else:
                return "Fourth", 4

        else:
            return "Invalid Wire Configuration", 0

    def reset(self):
        self.wires = []
        