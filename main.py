# Import GUI elements
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.textinput import TextInput
from kivy.config import Config

from models import Bomb

# Create a bomb for the game to use
gameBomb = Bomb.Bomb()

class StartScreen(Widget):
    pass

class BombScreen(BoxLayout):
    # Initialise the BombScreen to use the parent BoxLayout properties
    def __init__(self, **args):
        super(BombScreen, self).__init__(**args)
        self.orientation = 'horizontal'
        self.size = self.width, self.height

        # Create the bomb view page, containing all the widgets that will be used to read values for the bomb
        bombValueWidgets = GridLayout()
        bombValueWidgets.cols = 2
        bombValueWidgets.rows = 6
        bombValueWidgets.size_hint = (0.7, 1)

        strikesLbl = Label(text = 'Strikes', font_size = 30)
        strikesTxBx = TextInput(
            text = '0',
            input_type = 'number',
            font_size = 50
        )

        self.btnStateBinMap = {"normafont_size = 50l" : False, "down" : True}

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
        lastSerialTxBx = TextInput(
            text = '0',
            input_type = 'number',
            multiline = False,
            id = 'serialNumber',
            font_size = 40
        )

        batteriesLabel = Label(text = 'Enter all batteries: ', font_size = 30)
        batteriesTxBx =  TextInput(
            text = "AA D", 
            multiline = True,
            id = 'batteries',
            font_size = 40
        )

        indicatorsLabel = Label(text = 'Indicators', font_size = 30)
        indicatorsTxBx = TextInput(
            text = 'FRK 1',
            multiline = True,
            font_size = 40
        )

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


        self.add_widget(bombValueWidgets)

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
        self.add_widget(navBar)

    def setBombToggleValue(self,instance):     
        setattr(gameBomb, instance.group, self.btnStateBinMap[instance.state])
        print(instance.group, getattr(gameBomb, instance.group))
        
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
        
        return BombScreen()


if __name__ == '__main__':
    KeepTalkingApp().run()