class Button():
    def __init__(self, bomb, colour, text):
        self.colour = colour
        self.text = text
        self.bomb = bomb

    def __repr__(self):
        return "Button: {} {}".format(self.colour, self.text)

    def __str__(self):
        return "Button: {} {}".format(self.colour, self.text)

    # Returns the action that the user has to perform on the button
    # to deactivate it. This is in the form of press and release or "# in any position"
    def solve(self):
        if(self.colour == "b" and self.text == "abort"):
            return "Timer has: {} in any position".format(self.ReleasingAHeldButton())
        elif(self.bomb.batteries.length > 1 and self.text == "detonate"):
             return "Press and Release"
        elif(self.colour == "w" and ["CAR", 1] in self.bomb.indicators):
             return "Timer has: {} in any position".format(self.ReleasingAHeldButton())
        elif(self.bomb.batteries.length > 2 and ["FRK", 1] in self.bomb.indicators):
            return "Press and Release"
        elif(self.colour == 'y'):
            return "Timer has: {} in any position".format(self.ReleasingAHeldButton())
        elif(self.colour = 'r' and self.text == "hold"):
            return "Press and Release"
        else:
            return "Timer has: {} in any position".format(self.ReleasingAHeldButton())

    # Returns the number that can appear on the timer at any posistion to solve the bomb
    # for the specified colour
    def ReleasingAHeldButton(self):
        colourTimerMap = {"Blue": 4, "White": 1, "Yellow": 5}

        if (self.colour in colourTimerMap):
            return colourTimerMap[self.colour]
        else:
            return 1

