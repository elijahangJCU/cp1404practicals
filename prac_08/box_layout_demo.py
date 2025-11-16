"""
Practical 8 Box Layout Demo
Estimated time to complete: 20 mins
Actual time taken to complete: 24 mins
"""

from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        return Builder.load_file("box_layout.kv")

    def handle_greet(self):
        name = self.root.ids.input_name.text
        self.root.ids.output_label.text = f"Hello {name}"

    def handle_clear(self):
        self.root.ids.input_name.text = ""
        self.root.ids.output_label.text = ""


if __name__ == "__main__":
    BoxLayoutDemo().run()

