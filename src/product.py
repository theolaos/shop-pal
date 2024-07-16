from kivy.uix.screenmanager import Screen, SlideTransition
from src.utils import switch_screen


class ProductScreen(Screen): 
    def __init__(self, **kw):
        super().__init__(**kw)