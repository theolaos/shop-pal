import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button

kivy.require("2.3.0")


class Products(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        for i in range(1,26):
            self.add_widget(
                Button(text=f"{1}", size_hint=(.2,.2))
            )

class Menu(BoxLayout): 
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.add_widget(Products())


class ShopPalApp(App):
    def build(self) -> None:
        return Menu()
    
    
shopPal = ShopPalApp()
shopPal.run()