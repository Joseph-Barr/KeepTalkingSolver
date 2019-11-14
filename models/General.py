# Similar to the function asking for Y/N, so could be combined later
# TODO: add more sanitisation for only letters (REGEX?)
def getLetterIn():
    userIn = input("Please enter a letter:\n")
    while(len(userIn) != 1):
        userIn = input("Please enter a letter:\n")
    return userIn.lower()

