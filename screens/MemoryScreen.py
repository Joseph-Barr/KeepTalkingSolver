from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

from models.General import SingleNumericTextInput
from models.Memory import Memory

from gameVars import gameBomb

class MemoryScreen(Screen):
    def __init__(self, **args):
        super(MemoryScreen, self).__init__(**args)
        self.currentStage = 1
        self.module = Memory()

        ScreenLayout = BoxLayout(orientation = 'vertical')

        self.promptLabel = Label(
            text = 'Enter the number on the display in the textbox below',
            font_size = 30,
            size_hint = (1, 0.5)
        )

        ScreenLayout.add_widget(self.promptLabel)

		# Subscreen manager for the switching between enterting the display number
		# and the pos / num values

        self.SubscreenManager = ScreenManager()
        displayNumScreen = Screen(name = 'displayNumScreen')
        posNumScreen = Screen(name = 'posNumScreen')
        
        # This group of widgets is for entering the position and the number
        inputGrid = GridLayout(cols = 2, rows = 2)
        
        # Labels for the input boxes
        inputGrid.add_widget(Label(text = 'Position', font_size = 40))
        inputGrid.add_widget(Label(text = 'Number', font_size = 40))

        self.inputPosition = SingleNumericTextInput(
            font_size = 20,
            multiline = False
        )
        self.inputNumber = SingleNumericTextInput(
            font_size = 20,
            multiline = False
        )

        inputGrid.add_widget(self.inputPosition)
        inputGrid.add_widget(self.inputNumber)

        posNumScreen.add_widget(inputGrid)

        # Entering the display number screen
        self.displayNumTxIn = SingleNumericTextInput(
            font_size = 50
        )

        displayNumScreen.add_widget(self.displayNumTxIn)

        # Add all the screens to screenmanager and add to main screenlayout
        self.SubscreenManager.add_widget(displayNumScreen)
        self.SubscreenManager.add_widget(posNumScreen)
        self.SubscreenManager.current = 'displayNumScreen'
        ScreenLayout.add_widget(self.SubscreenManager)

        nextButton = Button(
            text = 'Next',
            size_hint = (1, 0.5)
        )
        nextButton.bind(on_release = self.nextStage)

        ScreenLayout.add_widget(nextButton)

        self.add_widget(ScreenLayout)

    def nextStage(self, instance):
        if self.currentStage > 5:
            print('Module Completed')
            # Do nothing if the module is completed
            return
        else:
            if self.SubscreenManager.current == 'displayNumScreen':
                self.promptLabel.text = self.module.getStage(self.currentStage, int(self.displayNumTxIn.text))
                self.SubscreenManager.current = 'posNumScreen'
            else:
                try:
                    self.module.setStage(self.currentStage, int(self.inputPosition.text), int(self.inputNumber.text))
                except ValueError:
                    print('Error converting Pos or Value to Int')
                    return
                self.promptLabel.text = 'What is the number on the display'
                self.SubscreenManager.current = 'displayNumScreen'


            self.currentStage += 1


