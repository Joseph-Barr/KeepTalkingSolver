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

    def __repr__(self):
        return self.code

    def __str__(self):
        return self.code

    def solve(self):
        pass

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