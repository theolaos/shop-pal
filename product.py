from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

from utils import switch_screen


class ProductScreen(Screen): 
    def __init__(self, **kw):
        super().__init__(**kw)

    def switch_screen_slide(self, name, direction, duration=.5):
        switch_screen(self,
            name, 
            SlideTransition(
                direction=direction, 
                duration=duration
            )
        )