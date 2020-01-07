from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

from models.Passwords import Password

from gameVars import gameBomb

class PasswordScreen(Screen):
    def __init__(self, **args):
        super(PasswordScreen, self).__init__(**args)
        self.inputLetters = []

        ScreenLayout = BoxLayout(orientation = 'vertical')

        ScreenLayout.add_widget(Label(
            text = 'Please Enter All Letters For Column'
        ))

        self.letterInputTxBx = TextInput()

        self.nextButton = Button(
            text = 'Next',
            font_size = 30
        )
        self.nextButton.bind(on_release = self.nextPasswordCol)
        
        self.possiblePasswordsLabel = Label(
            text = 'Possible Passwords'
        )

        ScreenLayout.add_widget(self.letterInputTxBx)
        ScreenLayout.add_widget(self.nextButton)
        ScreenLayout.add_widget(self.possiblePasswordsLabel)

        self.add_widget(ScreenLayout)

    def nextPasswordCol(self, instance):
        self.inputLetters.append(self.letterInputTxBx.text)
        self.letterInputTxBx.text = ''
        print(self.inputLetters)