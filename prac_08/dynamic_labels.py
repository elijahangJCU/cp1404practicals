"""
Practical 8 Dynamic Labels
Estimated time to complete: 35 mins
Actual time taken to complete: 29 mins
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Elijah", "James", "Lindsay", "Cynthia", "Chan"]

    def build(self):
        self.title = "Dynamic Labels"
        root = Builder.load_file("dynamic_labels.kv")

        for name in self.names:
            # FINAL version of the dynamic label
            temp_label = Label(
                text=name,
                font_size=32,
                size_hint_y=1,   # <<< THIS MAKES THEM EVENLY SPREAD
                halign="center",
                valign="middle"
            )
            temp_label.bind(size=temp_label.setter("text_size"))
            root.ids.main.add_widget(temp_label)

        return root


if __name__ == "__main__":
    DynamicLabelsApp().run()

