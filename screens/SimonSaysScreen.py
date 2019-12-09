from kivy.uix.screenmanager import Screen
from kivy.properties import ListProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.textinput import TextInput

from models.SimonSays import SimonSays

class SimonSaysScreen(Screen):
    def __init__(self, bomb, **args):
        super(SimonSaysScreen, self).__init__(**args)

        self.bomb = bomb

        ScreenLayout = BoxLayout(orientation = 'vertical')

        self.ColourGrid = GridLayout(cols = 3, rows = 4, size_hint = (1, 0.85))
        ScreenLayout.add_widget(self.ColourGrid)
        self.module = SimonSays(self.bomb)

        # Provide a default colour map where each colour is itself
        self.colourMap = {"Red" : "Red", "Blue" : "Blue", "Green" : "Green", "Yellow" : "Yellow"}

        # Dict of output text labels
        self.outputLabelDict = {"Red" : Label(), "Blue" : Label(), "Green" : Label(), "Yellow" : Label()}

        colourToRGB = {"Red" : ListProperty([1, 0, 0, 1]), "Blue" : ListProperty([0, 0, 1, 1]), "Green" : ListProperty([0, 1, 0, 1]), "Yellow" : ListProperty([1, 1, 0, 1])}

        self.colourMap = self.module.getMap()

        for colour in self.colourMap:
            colourInputLabel = Label(
                text = colour
            )
            
            self.ColourGrid.add_widget(colourInputLabel)
            self.ColourGrid.add_widget(Label(text = 'Becomes -> '))

            self.outputLabelDict[colour].text = self.colourMap[colour]
            
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
        self.module.getMap()
        for outputLabel in self.outputLabelDict:
            self.outputLabelDict[outputLabel].text = self.colourMap[outputLabel]