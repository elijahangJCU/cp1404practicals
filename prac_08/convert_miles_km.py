"""
Practical 8 Convert Miles to KM
Estimated time to complete: 35 mins
Actual time taken to complete: 40 mins
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934    # conversion constant


class ConvertMilesKmApp(App):
    """App to convert miles to kilometres using MVC structure."""

    km_output = StringProperty("0.0")

    def build(self):
        """Load .kv file and return the root widget."""
        self.title = "Convert Miles to Kilometres"
        return Builder.load_file("convert_miles_km.kv")


    # Helper to safely convert text
    def get_valid_miles(self, miles_text):
        """Return miles as float, or 0.0 if invalid."""
        try:
            return float(miles_text)
        except ValueError:
            return 0.0


    # Button: Convert
    def handle_convert(self, miles_text):
        miles = self.get_valid_miles(miles_text)
        km = miles * MILES_TO_KM
        self.km_output = f"{km:.5f}"


    # Buttons: Up / Down
    def handle_increment(self, miles_text, change):
        miles = self.get_valid_miles(miles_text)
        miles += change
        self.root.ids.input_miles.text = str(miles)
        self.handle_convert(str(miles))  # auto-convert after changing value


    # on_text: convert immediately
    def text_changed(self, miles_text):
        miles = self.get_valid_miles(miles_text)
        km = miles * MILES_TO_KM
        self.km_output = f"{km:.5f}"


if __name__ == "__main__":
    ConvertMilesKmApp().run()
