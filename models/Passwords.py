#from General import getLetterArrayIn
import re as Regex
def getLetterArrayIn(strLength = 0, validLetters = "abcdefghijklmnopqrstuvwxyz"):
    userIn = input("Please enter all letters:\n")
    userIn = userIn.lower()

    validLettersRegex = "[^%s]" % validLetters
    regexFind = Regex.search(validLettersRegex, userIn)

    while(bool(regexFind)):
        userIn = input("Please enter all letters:\n")
        userIn = userIn.lower()
        regexFind = Regex.search(validLettersRegex, userIn)

    return userIn.lower()

class Password():
    def __init__(self):
        # Store a list of all possible passwords
        self.passwords = ['after', 'again', 'below', 'could', 'every', 'first', 'found', 'great', 'house', 'large', 'learn', 'never', 'other', 'place', 'plant', 'point', 'right', 'small', 'sound', 'spell', 'still', 'study', 'their', 'there', 'these', 'thing', 'think', 'three', 'water', 'where', 'which', 'world', 'would', 'write']
        # Store a copy of the passwords list representing what the module thinks the passwords could be
        self.state = self.passwords

    def __repr__(self):
        return self.state
    
    def __str__(self):
        output = "Current Possible Passwords: "
        for password in self.state:
            output += "{}, ".format(password)
        return output[:-2]

    def solve(self, letterList):
        currIndex = 0
        for letters in letterList:
            tempSearch = []
            for password in self.state:
                for letter in letters:
                    if (password[currIndex] == letter):
                        tempSearch.append(password)
            currIndex += 1
            self.state = tempSearch
        print("There are {} possible passwords".format(len(self.state)))
        print(self.state)
        return self.state