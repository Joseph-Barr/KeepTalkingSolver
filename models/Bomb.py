class Bomb():
    def __init__(self, strikes = 0, parallel = False, serialVowel = False, lastSerialDigit = 0, batteries = [], indicators = []):
        self.strikes = strikes
        self.parallel = parallel
        self.serialVowel = serialVowel
        self.lastSerialDigit = lastSerialDigit
        self.batteries = batteries
        self.indicators = indicators
