"""
CP1404/CP5632 Practical
Kivy GUI program to square a number
Estimated time taken to complete: 20 mins
Actual time taken to complete: 20 mins
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = "Elijah Ang"


class SquareNumberApp(App):
    """ Kivy app for squaring a number """

    def build(self):
        """ Build the Kivy app from the kv file """
        Window.size = (300, 150)
        self.title = "Square Number"
        self.root = Builder.load_file('squaring.kv')
        return self.root

    def handle_calculate(self, value):
        """ Handle calculate button press or call """
        try:
            result = float(value) ** 2
            self.root.ids.output_label.text = str(result)
        except ValueError:
            self.root.ids.output_label.text = "0"


SquareNumberApp().run()