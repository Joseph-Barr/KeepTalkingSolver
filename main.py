# Import GUI elements
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.config import Config

from models import Bomb


class StartScreen(Widget):
    pass
        
class KeepTalkingApp(App):

    def build(self):
        Config.set('graphics', 'width', '800')
        Config.set('graphics', 'height', '600')
        
        return StartScreen()


if __name__ == '__main__':
    KeepTalkingApp().run()