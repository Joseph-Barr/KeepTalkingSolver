import re as Regex

# Similar to the function asking for Y/N, so could be combined later
# TODO: add more sanitisation for only letters (REGEX?)
def getLetterArrayIn(strLength = 0, validLetters):
    userIn = input("Please enter all letters:\n")
    userIn = userIn.lower()

    validLettersRegex = "[^%s]" % validLetters
    regexFind = Regex.search(validLettersRegex, userIn)

    while(bool(regexFind)):
        userIn = input("Please enter all letters:\n")
        userIn = userIn.lower()
        regexFind = Regex.search(validLettersRegex, userIn)

    return output.lower()