# Import GUI elements
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.textinput import TextInput
from kivy.config import Config

from models.Bomb import Bomb
from gameVars import gameBomb as gameBomb
from screens.ButtonScreen import ButtonScreen
from screens.SimonSaysScreen import SimonSaysScreen
from screens.WhosOnFirstScreen import WhosOnFirstScreen
from screens.MemoryScreen import MemoryScreen
from screens.MorseCodeScreen import MorseCodeScreen
from screens.PasswordScreen import PasswordScreen
import re as Regex

from models.General import SingleNumericTextInput


# Define the main screen that contains the bomb variables
class BombScreen(Screen):
    # Initialise the BombScreen to use the parent BoxLayout properties
    def __init__(self, **args):
        super(BombScreen, self).__init__(**args)

        ScreenLayout = BoxLayout(size = (self.width, self.height), orientation = 'horizontal')

        # Create the bomb view page, containing all the widgets that will be used to read values for the bomb
        bombValueWidgets = GridLayout()
        bombValueWidgets.cols = 2
        bombValueWidgets.rows = 6
        bombValueWidgets.size_hint = (0.7, 1)

        strikesLbl = Label(text = 'Strikes', font_size = 30)
        strikesTxBx = SingleNumericTextInput(
            id = 'strikes',
            text = '0',
            font_size = 60,
            multiline = False
        )
        strikesTxBx.bind(focus = onFocusSetIntAttr)

        self.btnStateBinMap = {"normal" : False, "down" : True}

        parallelLabel = Label(text = 'Parallel Port?: ', font_size = 30)
        parallelTg = ToggleButton(
            text = 'Yes/No',
            group = 'parallel',
            on_press = self.setBombToggleValue
        )

        serialNumLabel = Label(text = "Does the Serial Number Have a Vowel?: ", font_size = 20)
        serialNumTg = ToggleButton(
            text = 'Yes/No',
            group = 'serialVowel',
            on_press = self.setBombToggleValue

        )

        lastSerialLabel = Label(text = "What is the last digit of the serial number?: ", font_size = 20, halign = 'right')
        lastSerialTxBx = SingleNumericTextInput(
            id = 'lastSerialDigit',
            text = '0',
            multiline = False,
            font_size = 60
        )
        lastSerialTxBx.bind(focus = onFocusSetIntAttr)


        batteriesLabel = Label(text = 'Enter all batteries: ', font_size = 30)
        batteriesTxBx =  TextInput(
            id = 'batteries',
            text = "AA D", 
            multiline = False,
            font_size = 40
        )
        batteriesTxBx.bind(focus = self.setBatteriesInput)


        indicatorsLabel = Label(text = 'Indicators', font_size = 30)
        indicatorsTxBx = TextInput(
            id = 'indicators',
            text = 'FRK 1',
            multiline = False,
            font_size = 30
        )
        indicatorsTxBx.bind(focus = self.setIndicatorsInput)

        # Fix all the widgets to the bomb widgets side of the screen grid
        bombValueWidgets.add_widget(strikesLbl)
        bombValueWidgets.add_widget(strikesTxBx)
        bombValueWidgets.add_widget(parallelLabel)
        bombValueWidgets.add_widget(parallelTg)
        bombValueWidgets.add_widget(serialNumLabel)
        bombValueWidgets.add_widget(serialNumTg)
        bombValueWidgets.add_widget(lastSerialLabel)
        bombValueWidgets.add_widget(lastSerialTxBx)
        bombValueWidgets.add_widget(batteriesLabel)
        bombValueWidgets.add_widget(batteriesTxBx)
        bombValueWidgets.add_widget(indicatorsLabel)
        bombValueWidgets.add_widget(indicatorsTxBx)


        ScreenLayout.add_widget(bombValueWidgets)

        # Send the layout of the screen to this class instance
        self.add_widget(ScreenLayout)
    
    def setBombToggleValue(self, instance):     
        setattr(gameBomb, instance.group, self.btnStateBinMap[instance.state])
        print(instance.group, getattr(gameBomb, instance.group))

    # Implement different sanitisation rules for indicators and batteries
    def setBatteriesInput(self, instance, value):
        possibleBatteries = ["AA", "D"]
        if not value:
            battList = instance.text.split(' ')
            try:
                for battery in battList:
                    if battery not in possibleBatteries:
                        raise Exception("Battery {} doesnt exist".format(battery))
                    else:
                        pass
                # If all the batteries are legit, set the batteries on the bomb
                gameBomb.batteries = battList
            except Exception:
                errMsg = "Error setting batteries {}".format(instance.text)
                print(errMsg)
                instance.text = errMsg
            print(gameBomb.batteries)
    
    def setIndicatorsInput(self, instance, value):
        possibleIndicators = ['SND', 'CLR', 'CAR', 'IND', 'FRQ', 'SIG', 'NSA', 'MSA', 'TRN', 'BOB', 'FRK']
        if not value:
            indicators = instance.text.upper()
            indicators = indicators.split(', ')

            try:
                for i, indAndState in enumerate(indicators):
                    temp = indAndState.split(' ')
                    if ((temp[0] not in possibleIndicators) or ((int(temp[1]) != 0) and (int(temp[1]) != 1))):
                        print(temp[0], int(temp[1]))
                        raise Exception('Invalid Indicators')
                    else: 
                        indicators[i] = temp
                        indicators[i][1] = int(indicators[i][1])
                gameBomb.indicators = indicators
                print(gameBomb.indicators)    
            
            except (Exception):
                instance.text = "Error in : '{}'".format(instance.text)
                print("Error splitting indicator values, nothing set")        

def onFocusSetIntAttr(instance, value):
    if value:
        pass
    else:
        try:
            setattr(gameBomb, instance.id, int(instance.text))
        except ValueError:
            print('Error setting value {} to {}'.format( instance.id, instance.text ))
        print(instance.id, ' : ',  instance.text)

def goToGameScreen(instance):
        try:
            ModuleScreenController.current = instance.id
        except Exception:
            print('Error loading screen {}'.format(instance.id))

# Setting the game screen
# This screen is the main screen for the game and contains the navbar
# and the changing module screens
GameScreen = Screen(name = 'GameScreen')

GameScreenLayout = BoxLayout(orientation = 'horizontal')

ModuleScreenController = ScreenManager(transition = NoTransition())
ModuleScreenController.size_hint = (0.7, 1)

# Creating all the game screens
ModuleScreenController.add_widget(BombScreen(name = 'bomb'))
ButtonModuleScreen = ButtonScreen(name = 'button')
ButtonModuleScreen.setBomb(gameBomb)
ModuleScreenController.add_widget(ButtonModuleScreen)

SimonSaysModuleScreen = SimonSaysScreen(name = 'simon says')
ModuleScreenController.add_widget(SimonSaysModuleScreen)

WhosOnFirstModuleScreen = WhosOnFirstScreen(name = 'whos on first')
ModuleScreenController.add_widget(WhosOnFirstModuleScreen)

MemoryModuleScreen = MemoryScreen(name = 'memory')
ModuleScreenController.add_widget(MemoryModuleScreen)

MorseCodeModuleScreen = MorseCodeScreen(name = 'morse code')
ModuleScreenController.add_widget(MorseCodeModuleScreen)

PasswordModuleScreen = PasswordScreen(name = 'passwords')
ModuleScreenController.add_widget(PasswordModuleScreen)

# Prepare the navbar
# Container for the nav bar buttons
navBar = BoxLayout(
    size_hint = (0.3, 1),
    orientation = 'vertical'
)
# Create a list of buttons and their names for the navbar
widgetList = ['bomb', 'button', 'memory', 'morse code', 'passwords', 'simon says', 'simple wires', 'whos on first']
for widget in widgetList:
    moduleButton = Button(
                        text = widget.capitalize(),
                        id = widget
                        )
    moduleButton.bind(on_release = goToGameScreen)
    navBar.add_widget(moduleButton)

# Add the 2 halves of the screen to the main layout
GameScreenLayout.add_widget(ModuleScreenController)
GameScreenLayout.add_widget(navBar)
# Add the layout to the displayed screen
GameScreen.add_widget(GameScreenLayout)



class KeepTalkingApp(App):

    def build(self):
        Window.size = (1200, 600)

        return GameScreen


if __name__ == '__main__':
    KeepTalkingApp().run()