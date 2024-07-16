from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

from utils import switch_screen


class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)