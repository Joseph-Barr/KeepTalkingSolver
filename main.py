# Import GUI elements
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.textinput import TextInput
from kivy.config import Config

from models import Bomb
import re as Regex

# Create a bomb for the game to use
gameBomb = Bomb.Bomb()

class WindowManager(ScreenManager):
    def __init__(self, **args):
        super(WindowManager, self).__init__(**args)
        self.add_widget(BombScreen(name = 'bombScreen'))

# Checks if the text in the text input is a number or not.
# Performs as normal if not, otherwise empties the instance
class SingleNumericTextInput(TextInput):
    def insert_text(self, substring, from_undo = False):
        searchRgx = Regex.compile('([0-9])')
        searchResult = searchRgx.fullmatch(substring)
        
        if (searchResult is not None):
            output = substring
        else:
            output = ""

        return super(SingleNumericTextInput, self).insert_text(output, from_undo = from_undo)


# Define the main screen that contains the bomb variables
class BombScreen(Screen):
    # Initialise the BombScreen to use the parent BoxLayout properties
    def __init__(self, **args):
        super(BombScreen, self).__init__(**args)
        #self.orientation = 'horizontal'
        #self.size = self.width, self.height

        ScreenLayout = GridLayout(cols = 3, rows = 1, size = (self.width, self.height))

        # Create the bomb view page, containing all the widgets that will be used to read values for the bomb
        bombValueWidgets = GridLayout()
        bombValueWidgets.cols = 2
        bombValueWidgets.rows = 6
        bombValueWidgets.size_hint = (0.7, 1)

        strikesLbl = Label(text = 'Strikes', font_size = 30)
        strikesTxBx = SingleNumericTextInput(
            id = 'strikes',
            text = '0',
            #on_focus = pass,
            font_size = 60,
            multiline = False
        )
        strikesTxBx.bind(focus = onFocusSetAttr)

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

        lastSerialLabel = Label(text = "What is the last digit of the serial number?: ", font_size = 20)
        lastSerialTxBx = SingleNumericTextInput(
            id = 'lastSerialDigit',
            text = '0',
            multiline = False,
            font_size = 60,
        )
        lastSerialTxBx.bind(focus = onFocusSetAttr)


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

        navBar = BoxLayout(
            size_hint = (0.3, 1),
            orientation = 'vertical'
        )
        widgetList = ['bomb', 'button', 'memory', 'morse code', 'passwords', 'simon says', 'simple wires', 'whos on first']
        for widget in widgetList:
            navBar.add_widget(Button(
                text = widget.capitalize(),
                id = widget
            ))
        ScreenLayout.add_widget(navBar)

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
            indicators = instance.text
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

def onFocusSetAttr(instance, value):
    if value:
        pass
    else:
        setattr(gameBomb, instance.id, instance.text)
        print(instance.text)

        
class navSideBar(GridLayout):
    def __init__(self, **args):
        super(navSideBar, self).__init__(**args)
        self.cols = 1
        self.rows = 6
        btn = Button(
            size_hint = (0.3, 1),
            text = str(self.width)
        )
        self.add_widget(btn)

class KeepTalkingApp(App):

    def build(self):
        Config.set('graphics', 'width', '1200')
        Config.set('graphics', 'height', '800')
        
        return WindowManager()


if __name__ == '__main__':
    KeepTalkingApp().run()