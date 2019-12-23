class Morse():
    wordToFreq = {
        "shell": 3.505,
        "halls": 3.515,
        "slick": 3.522,
        "trick": 3.532,
        "boxes": 3.535,
        "leaks": 3.542,
        "strobe": 3.545,
        "bistro": 3.552,
        "flick": 3.555,
        "bombs": 3.565,
        "break": 3.572,
        "brick": 3.575,
        "steak": 3.582,
        "sting": 3.592,
        "vector": 3.595,
        "beats": 3.600
    }

    # The constructor for this module takes a morse code string in the form ".. ..", where the space represents a gap between words
    def __init__(self, morseCode):
        # self.code contains the individual letters of the morse code
        self.code = morseCode.split()
        self.frequency = 0.0

    def __repr__(self):
        output = ""
        for char in self.code:
            output += char
        return output

    def __str__(self):
        output = ""
        for char in self.code:
            output += char
        return output

    # Returns a list of possible values for the given sequence of morse code characters
    def solve(self):
        string = ""
        for morseChar in self.code:
            string += convertMorseToChar(morseChar)

        possibleValues = []

        for word in self.wordToFreq:
            # Detect if there are more found characters than not found, gives some basic error correction
            charsInWord = 0
            charsNotInWord = 0
            for char in string:
                if char not in word:
                    charsNotInWord += 1
                else:
                    charsInWord += 1

            if charsNotInWord < charsInWord:
                possibleValues.append([word, self.wordToFreq[word]])
        
        return possibleValues

# Returns a character for the given morse code
def convertMorseToChar(morse):
    morseCharMap = {
        ".-": 'a',
        "-...": 'b',
        "-.-.": 'c',
        "-..": 'd',
        ".": 'e',
        "..-.": 'f',
        "--.": 'g',
        "....": 'h',
        "..": 'i',
        ".---": 'j',
        "-.-": 'k',
        ".-..": 'l',
        "--": 'm',
        "-.": 'n',
        "---": 'o',
        ".--.": 'p',
        "--.-": 'q',
        ".-.": 'r',
        "...": 's',
        "-": 't',
        "..-": 'u',
        "...-": 'v',
        ".--": 'w',
        "-..-": 'x',
        "-.--": 'y',
        "--..": 'z',
        "-----": '0',
        ".----": '1',
        "..---": '2',
        "...--": '3',
        "....-": '4',
        ".....": '5',
        "-....": '6',
        "--...": '7',
        "---..": '8',
        "----.": '9'
    }

    return morseCharMap[morse]
