from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.textinput import TextInput
from kivy.uix.modalview import ModalView


from models.General import ColouredLabel
from models.SimpleWires import SimpleWires

from gameVars import gameBomb as gameBomb

class SimpleWiresScreen(Screen):
    def __init__(self, **args):
        super(SimpleWiresScreen, self).__init__(**args)
        
        # Store the sequence of colours
        self.currentSequence = []

        screenLayout = BoxLayout(orientation = "vertical")
        
        buttonLayout = BoxLayout(orientation = "horizontal")
        # Red Button
        self.redButton = Button(
            text = "Red",
            background_normal = '',
            background_color = (1, 0, 0, 1)
        )
        self.redButton.bind(on_release = self.addColourToModule)
        # Blue Button
        self.blueButton = Button(
            text = "Blue",
            background_normal = "",
            background_color = (0, 0, 1, 1)
        )
        self.blueButton.bind(on_release = self.addColourToModule)
        # White Button
        self.whiteButton = Button(
            text = "White",
            background_normal = '',
            color = (0, 0, 0, 1),
            background_color = (1, 1, 1, 1)
        )
        self.whiteButton.bind(on_release = self.addColourToModule)

        # Yellow Button
        self.yellowButton = Button(
            text = "Yellow",
            background_normal = "",
            color = (0, 0, 0, 1),
            background_color = (1, 1, 0, 1)
        )
        self.yellowButton.bind(on_release = self.addColourToModule)

        # Black Button
        self.blackButton = Button(
            text = "Black",
            color = (1, 1, 1, 1),
            background_normal = "",
            background_color = (0, 0, 0, 1)
        )
        self.blackButton.bind(on_release = self.addColourToModule)
        buttonLayout.add_widget(self.redButton)
        buttonLayout.add_widget(self.blueButton)
        buttonLayout.add_widget(self.whiteButton)
        buttonLayout.add_widget(self.yellowButton)
        buttonLayout.add_widget(self.blackButton)

        screenLayout.add_widget(buttonLayout)

        # Label that shows the current colour sequence
        self.currentSeqLabel = Label(
            text = "Current Sequence: "
        )
        screenLayout.add_widget(self.currentSeqLabel)

        # Solve and reset buttons
        solveResetBox = BoxLayout(orientation = 'horizontal')
        self.solveButton = Button(
            text = 'Solve'
        )
        self.solveButton.bind(on_release = self.solveModule)
        self.resetButton = Button(
            text = 'Reset'
        )
        self.resetButton.bind(on_release = self.resetModule)
        solveResetBox.add_widget(self.solveButton)
        solveResetBox.add_widget(self.resetButton)

        screenLayout.add_widget(solveResetBox)

        # Results modal
        self.resultsModal = ModalView(size_hint = (0.5, 0.5))
        self.resultsLabel = Label(
            text = "Cut:"
        )
        self.resultsModal.add_widget(self.resultsLabel)

        self.add_widget(screenLayout)

    def addColourToModule(self, instance):
        self.currentSequence.append(instance.text)
        self.currentSeqLabel.text = "Current Sequence: {}".format(self.currentSequence)

    def resetModule(self, instance):
        self.currentSequence = []
        self.currentSeqLabel.text = "Sequence Reset"

    def solveModule(self, instance):
        colorCompatList = {"Black": 'bk', "Blue": "bl", "Yellow": "y", "Red": "r", "White": 'w'}
        convSeq = []
        
        for wire in range(0, len(self.currentSequence)):
            convSeq.append(colorCompatList[self.currentSequence[wire]])
        simpleWires = SimpleWires(gameBomb)
        result = simpleWires.solve(convSeq)
        if result[1] != 0:
            self.resultsLabel.text = "Cut the {} wire".format(result[0])
        else:
            self.resultsLabel.text = result[0]
        self.resultsModal.open()