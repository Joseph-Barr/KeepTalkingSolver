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

        self.nextButton = Button(
            text = 'Next',
            size_hint = (1, 0.5)
        )
        self.nextButton.bind(on_release = self.nextStage)

        ScreenLayout.add_widget(self.nextButton)

        self.add_widget(ScreenLayout)

    def nextStage(self, instance):
        if self.currentStage > 5:
            return
        else:
            if self.SubscreenManager.current == 'displayNumScreen':
                try:
                    dispIn = int(self.displayNumTxIn.text)
                    if not checkWithinRange(1, 4, dispIn):
                        print('Value Too High')
                        return
                    self.promptLabel.text = self.module.getStage(self.currentStage, dispIn)
                    self.SubscreenManager.current = 'posNumScreen'
                    # Set the text for the button to reset when it appears on the next module
                    if self.currentStage == 5:
                        self.nextButton.text = 'Reset'

                except ValueError:
                    print('Error Converting number to Int')
                    return
                # TODO ADD QOL changes to make the text box contain the variable that the player does not have to find because it is known
            else:
                try:
                    posIn = int(self.inputPosition.text)
                    numIn = int(self.inputNumber.text)
                    
                    if not checkWithinRange(1, 4, posIn) or not checkWithinRange(1, 4, numIn):
                        print('Value Too High')
                        return

                    if self.currentStage != 5:
                        self.module.setStage(self.currentStage, posIn, numIn)
                    self.currentStage += 1
                    self.promptLabel.text = 'What is the number on the display'
                    self.SubscreenManager.current = 'displayNumScreen'
                except ValueError:
                    print('Error converting Pos or Value to Int')
                    return

        if self.currentStage > 5:
            # IF the module is complete make the next button a reset button
            print('Module Completed')
            print('Resetting Module')
            self.module = Memory()
            self.currentStage = 1
            self.nextButton.text = 'Next'

        print(self.module.state, self.currentStage)

def checkWithinRange(lower, upper, num):
    if num < lower or num > upper:
        return False
    else: 
        return True

            
            


