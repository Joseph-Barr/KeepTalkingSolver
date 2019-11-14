# Similar to the function asking for Y/N, so could be combined later
# TODO: add more sanitisation for only letters (REGEX?)
def getLetterArrayIn():
    userIn = input("Please enter all letters:\n")
    userIn = userIn.lower()

    # Make sure all the letters are unique
    output = ""
    for letter in userIn:
        if (letter not in output):
            output += "{}".format(letter)
    return output.lower()