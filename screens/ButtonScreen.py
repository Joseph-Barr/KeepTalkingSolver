from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.textinput import TextInput

from models.Button import Button as ButtonModule

class ButtonScreen(Screen):
    def __init__(self, **args):
        super(ButtonScreen, self).__init__(**args)
        ScreenLayout = BoxLayout(orientation = 'vertical', padding = 20)

        LabelInGrid = GridLayout(cols = 2, rows = 2)
        # Labels and inputs
        LabelInGrid.add_widget(Label(text = 'Colour: ', font_size = 40))
        LabelInGrid.add_widget(Label(text = 'Text: ', font_size = 40))
        self.ButtonColourTxIn = TextInput(
            font_size = 40,
            text = 'Eg. Blue',
            multiline = False
        )
        self.ButtonTextTxIn = TextInput(
            font_size = 40,
            text = 'Eg. Explode',
            multiline = False
        )
        LabelInGrid.add_widget(self.ButtonColourTxIn)
        LabelInGrid.add_widget(self.ButtonTextTxIn)

        ScreenLayout.add_widget(LabelInGrid)

        solveButton = Button(
            text = 'Solve',
            id = 'solveButton'
        )
        solveButton.bind(on_release = self.getSolve)
        ScreenLayout.add_widget(solveButton)

        self.resultsLbl = Label(
            text = 'Press Solve',
            font_size = 35
        )
        ScreenLayout.add_widget(self.resultsLbl)
        self.add_widget(ScreenLayout)


    # Defining helper functions for the class
    # Gets and displays the results of the solve
    def getSolve(self, instance):
        try:
            b = ButtonModule(self.bomb, self.ButtonColourTxIn.text[0].lower(), self.ButtonTextTxIn.text.lower())
            print(b.bomb, b.colour, b.text)
            self.resultsLbl.text = str(b.solve())
        except IndexError:
            self.resultsLbl.text = 'Please enter colour and text'
        except Exception:
            print(Exception)
            self.resultsLbl.text = 'Unexpected error'
            

    # Sets the bomb, must be called because the init function cant contain a bomb
    def setBomb(self, bomb):
        self.bomb = bomb
