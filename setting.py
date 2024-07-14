from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

from utils import switch_screen


class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text="Settings Page"))
        layout.add_widget(
            Button(
                text="Back to Home", 
                on_press=switch_screen(self,
                    'home', 
                    transition=SlideTransition(
                        direction="left", 
                        duration=.5
                    )
                )
            )
        )
        self.add_widget(layout)