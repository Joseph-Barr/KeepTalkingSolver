from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

from models.WhosOnFirst import WhosOnFirst
from gameVars import gameBomb as gameBomb

class WhosOnFirstScreen(Screen):
    def __init__(self, **args):
        super(WhosOnFirstScreen, self).__init__(**args)

        self.module = WhosOnFirst()

        self.screenState = 0
        self.displayWordToPos = ''

        ScreenLayout = BoxLayout(orientation = "vertical", padding = 20)

        self.promptLabel = Label(text = 'Word on the display?: ', font_size = 40)

        self.answerText = TextInput(
            multiline = False,
            font_size = 30
        )
    
        submitButton = Button(
            text = 'Submit'
        )
        submitButton.bind(on_release = self.submit)

        ScreenLayout.add_widget(self.promptLabel)
        ScreenLayout.add_widget(self.answerText)
        ScreenLayout.add_widget(submitButton)

        self.add_widget(ScreenLayout)

        self.resultsPopup = Popup(
            title = 'Results',
            content = Label(text = 'Results are supposed to be here'),
            size_hint = (0.75, 0.75)
        )    

    
    def submit(self, instance):
        userInput = self.answerText.text.lower()
        if self.screenState == 0:
            self.displayWordToPos = userInput
            getPosResult = self.module.getPos(self.displayWordToPos)
            if getPosResult[0] != 0:
                self.promptLabel.text = 'What is the word in the {}'.format(getPosResult[1])
                self.screenState = 1
                print(self.displayWordToPos)
            else:
                errMsg = 'Error: {}'.format(getPosResult[1])
                self.promptLabel.text = errMsg
                print(errMsg)
        else:
            print(self.answerText.text)
            try:
                self.resultsPopup.content = Label(text = 'Ready maps to:\n{}'.format(self.module.solve(userInput)), font_size = 20)
                self.resultsPopup.open()
                self.promptLabel.text = 'Word on the display?: '
                self.screenState = 0
            except KeyError:
                errMsg = 'Error with word: {}\nWord on the display?: '.format(userInput)
                self.promptLabel.text = errMsg
                print(errMsg)
