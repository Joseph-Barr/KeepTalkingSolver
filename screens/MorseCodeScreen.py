from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

from models.General import MorseTextInput
from models.MorseCode import Morse

from gameVars import gameBomb

class MorseCodeScreen(Screen):
    def __init__(self, **args):
        super(MorseCodeScreen, self).__init__(**args)
 
        ScreenLayout = BoxLayout(orientation = 'vertical')

        ScreenLayout.add_widget(Label(
            text = 'Morse Code: '
        ))

        self.userMorseTxIn = MorseTextInput(
            multiline = False
        )

        self.solveButton = Button(
            text = 'Solve',
            size_hint = (0.20, 1)
        )
        self.solveButton.bind(on_release = self.solveMorse)
    
        morseAndSolveGrid = GridLayout(cols = 2, rows = 1)
        morseAndSolveGrid.add_widget(self.userMorseTxIn)
        morseAndSolveGrid.add_widget(self.solveButton)
        ScreenLayout.add_widget(morseAndSolveGrid)

        self.outputLabel = Label(
            text = 'Possible Outputs ???'
        )
        
        ScreenLayout.add_widget(self.outputLabel)

        self.add_widget(ScreenLayout)

    def solveMorse(self, instance):
        morse = Morse(str(self.userMorseTxIn.text))
        possibleOutputsMorse = str(morse.solve())
        print(possibleOutputsMorse)
        if possibleOutputsMorse == '[]':
            outputText = 'No Valid Results Found'
        else:
            outputText = possibleOutputsMorse
        self.outputLabel.text = outputText