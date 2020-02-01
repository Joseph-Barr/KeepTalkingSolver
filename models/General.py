import re as Regex

# Similar to the function asking for Y/N, so could be combined later
# TODO: add more sanitisation for only letters (REGEX?)
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


from kivy.uix.textinput import TextInput
# Checks if the text in the text input is a number or not.
# Performs as normal if not, otherwise empties the instance
class SingleNumericTextInput(TextInput):
    def insert_text(self, substring, from_undo = False):
        searchRgx = Regex.compile('([0-9])')
        searchResult = searchRgx.fullmatch(substring)
        
        if (searchResult is not None):
            output = substring
        else:
            output = ""

        return super(SingleNumericTextInput, self).insert_text(output, from_undo = from_undo)

class MorseTextInput(TextInput):
    def insert_text(self, substring, from_undo = False):
        searchRgx = Regex.compile(r'([\-\. ]+)')
        searchResult = searchRgx.fullmatch(substring)
        
        if (searchResult is not None):
            output = substring
        else:
            output = ""

        return super(MorseTextInput, self).insert_text(output, from_undo = from_undo)

from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
class ColouredLabel(Label):
    def setBackground(self, r, g, b, a):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(r, g, b, a)
            self.rect = Rectangle(pos = self.pos, size = self.size)
        
        self.bind(pos = self.updateRect, size = self.updateRect)
    
    def updateRect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size