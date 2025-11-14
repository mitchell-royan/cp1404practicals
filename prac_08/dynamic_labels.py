"""
CP1404 - Practical 8
Dynamic Labels Program
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """App that displays dynamically created list of names"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Mitchell", "Bob", "Lindsay", "Ethan", "Someone else"]

    def build(self):
        """Build GUI from kv file"""
        root = Builder.load_file("dynamic_labels.kv")
        main_layout = root.ids.main
        for name in self.names:
            label = Label(text=name, font_size=24)
            main_layout.add_widget(label)
        return root


DynamicLabelsApp().run()


