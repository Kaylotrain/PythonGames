from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class BLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        b1 = Button(text="H")
        b2 = Button(text="H2")
        self.add_widget(b1)
        self.add_widget(b2)

class MainWidget(Widget):
    pass

class MyApp(App):
    pass

MyApp().run()