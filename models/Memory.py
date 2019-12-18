class Memory():
    # Memory contains a state that has the previous results stored in the form of [pos, number]
    # Calling self.state takes the form: self.state[stage - 1][pos = 0 / number = 1], eg stage 1 pos = self.state[0][0]
    # Memory also cannot contain a solve module because it relies solely on values from previous iterations
    def __init__(self):
        self.state = [[0, 0], [0, 0], [0, 0], [0, 0]]

    def __repr__(self):
        return self.state

    def __str__(self):
        return self.state
    
    # Returns the action the player must perform to disarm the module
    # Stage is the actual stage number the player is currently on (1 - 5)
    # Display is the number currently on the module screen
    def getStage(self, stage, display):
        # Array containing the result in the form stages[stage][display]
        stages = [
            ["Position 2", "Position 2", "Position 3", "Position 4"],
            ["Labelled 4", "Position {}".format(self.state[0][0]), "Position 1", "Position {}".format(self.state[0][0])],
            ["Labelled {}".format(self.state[1][1]), "Labelled {}".format(self.state[0][1]), "Position 3", "Labelled 4"],
            ["Position {}".format(self.state[0][0]), "Position 3", "Position {}".format(self.state[1][0]), "Position {}".format(self.state[1][0])],
            ["Labelled {}".format(self.state[0][1]), "Labelled {}".format(self.state[1][1]), "Labelled {}".format(self.state[3][1]), "Labelled {}".format(self.state[2][1])]
        ]
        
        return stages[stage - 1][display - 1]

    # Set modules stage values pos and val
    def setStage(self, stage, pos, val):
        if (pos > 4 or pos < 1) or (val > 4 or val < 1):
            return
        self.state[stage - 1] = [pos, val]