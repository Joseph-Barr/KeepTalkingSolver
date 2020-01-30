from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.uix.gridlayout import GridLayout
from kivy.uix.modalview import ModalView
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
        
        self.pleaseEnterLabel = Label(
            text = 'Please Enter All Letters For Column'
        )
        ScreenLayout.add_widget(self.pleaseEnterLabel)

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

        self.resetButton = Button(text = "Reset")
        self.resetButton.bind(on_release = self.reset)
        # Reset button modal
        self.resetModal = ModalView(size_hint = (0.4, 0.4))
        modalLayout = BoxLayout(
            orientation = "vertical"
        )
        modalLayout.add_widget(Label(
            text = "There are no available passwords"
        ))
        modalLayout.add_widget(self.resetButton)
        self.resetModal.add_widget(modalLayout)

    def nextPasswordCol(self, instance):
        self.inputLetters.append(self.letterInputTxBx.text.lower())
        self.letterInputTxBx.text = ''
        passwordPass = Password()
        passwordPass.solve(self.inputLetters)
        
        if len(passwordPass.state) == 0:
            self.possiblePasswordsLabel.text = 'There are no possible passwords'
            self.resetModal.open()
            
        else:
            self.possiblePasswordsLabel.text = str(passwordPass.state)

        self.pleaseEnterLabel.text = "Please Enter All Letters For Column {}".format(len(self.inputLetters) + 1)
        # TODO: Add reset button
    
    def reset(self, instance):
        self.inputLetters = []
        self.pleaseEnterLabel.text = "Please Enter All Letters For Column 1"
        self.resetModal.dismiss()