#from General import getLetterArrayIn

class SimpleWires():
    def __init__(self, bomb):
        self.bomb = bomb

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
    
    # Solves for sequenceList
    # Returns the position of the wire to cut as both a string and a integer eg ("Last", 3)
    def solve(self, sequenceList):
        # Implement the long list of rules for simple wires
        if(len(sequenceList) == 3):
            if("r" not in sequenceList):
                return "Second", 2
            elif(sequenceList[-1] == 'w'):
                return "Last", len(sequenceList)
            elif(sequenceList.count('bl') > 1):
                return "Last Blue", sequenceList.rfind('b') + 1
            else:
                return "Last", len(sequenceList)

        elif(len(sequenceList) == 4):
            if(sequenceList.count('r') > 1 and self.bomb.lastSerialDigit % 2 != 0):
                return "Last Red", sequenceList.rfind('r')
            elif(sequenceList[-1] == 'y' and sequenceList.count('r') == 0):
                return "First", 1
            elif(sequenceList.count('bl') == 1):
                return "First", 1
            elif(sequenceList.count('y') > 1):
                return "Last", len(sequenceList)
            else:
                return "Second", 2

        elif(len(sequenceList) == 5):
            if(sequenceList[-1] == 'bk' and self.bomb.lastSerialDigit % 2 != 0):
                return "Fourth", 4
            elif(sequenceList.count('r') == 1 and sequenceList.count('y') > 1):
                return "First", 1
            elif(sequenceList.count('bk') == 0):
                return "Second", 2
            else:
                return "First", 1

        elif(len(sequenceList) == 6):
            if(sequenceList.count('y') == 0 and self.bomb.lastSerialDigit % 2 != 0):
                return "Third", 3
            elif(sequenceList.count('y') == 1 and sequenceList.count('w') > 1):
                return "Fourth", 4
            elif(sequenceList.count('r') == 0):
                return "Last", len(sequenceList)
            else:
                return "Fourth", 4

        else:
            return "Invalid Wire Configuration", 0