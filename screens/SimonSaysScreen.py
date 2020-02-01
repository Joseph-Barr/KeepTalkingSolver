from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.textinput import TextInput


from models.SimonSays import SimonSays
from models.General import ColouredLabel

from gameVars import gameBomb as gameBomb

class SimonSaysScreen(Screen):
    def __init__(self, **args):
        super(SimonSaysScreen, self).__init__(**args)

        self.bomb = gameBomb

        ScreenLayout = BoxLayout(orientation = 'vertical')

        self.ColourGrid = GridLayout(cols = 3, rows = 4, size_hint = (1, 0.85))
        ScreenLayout.add_widget(self.ColourGrid)
        self.module = SimonSays(self.bomb)

        # Provide a default colour map where each colour is itself
        self.colourMap = {"Red" : "Red", "Blue" : "Blue", "Green" : "Green", "Yellow" : "Yellow"}

        # Dict of output text labels
        self.outputLabelDict = {"Red" : ColouredLabel(), "Blue" : ColouredLabel(), "Green" : ColouredLabel(), "Yellow" : ColouredLabel()}

        self.colourToRGB = {"Red" : [1, 0, 0, 0.5], "Blue" : [0, 0, 1, 0.5], "Green" : [0, 1, 0, 0.5], "Yellow" : [1, 1, 0, 0.5]}

        self.colourMap = self.module.getMap()

        for colour in self.colourMap:
            colourInputLabel = ColouredLabel(
                text = colour
            )
            colourSplit = self.colourToRGB[colour]
            colourInputLabel.setBackground(colourSplit[0], colourSplit[1], colourSplit[2], colourSplit[3])
            
            self.ColourGrid.add_widget(colourInputLabel)
            self.ColourGrid.add_widget(Label(text = 'Becomes -> '))

            self.outputLabelDict[colour].text = self.colourMap[colour]
            # Reuse the variable from before to get the RGBA value for the label colour 
            colourSplit = self.colourToRGB[self.colourMap[colour]]
            self.outputLabelDict[colour].setBackground(colourSplit[0], colourSplit[1], colourSplit[2], colourSplit[3])
            
            self.ColourGrid.add_widget(self.outputLabelDict[colour])

        refreshButton = Button(
            text = 'Refresh',
            size_hint = (1, 0.15)
        )
        refreshButton.bind(on_release = self.refreshLabels)
        ScreenLayout.add_widget(refreshButton)
        self.add_widget(ScreenLayout)

    def setBomb(self, bomb):
        self.bomb = bomb

    def refreshLabels(self, instance):
        self.module = SimonSays(gameBomb)
        self.module.mapColours()
        self.colourMap = self.module.getMap()
        for outputLabel in self.outputLabelDict:
            self.outputLabelDict[outputLabel].text = self.colourMap[outputLabel]

            colourSplit = self.colourToRGB[self.outputLabelDict[outputLabel].text]
            self.outputLabelDict[outputLabel].setBackground(colourSplit[0], colourSplit[1], colourSplit[2], colourSplit[3])
        print("Strikes: {}, serialVowel: {}, Colour Map: {}".format(gameBomb.strikes, gameBomb.serialVowel, self.colourMap))
