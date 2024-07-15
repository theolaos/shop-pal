import kivy
import os

from kivy.uix.screenmanager import ScreenManager, SlideTransition
from kivy.app import App
from kivy.lang import Builder

from home import HomeScreen
from cart import CartScreen
from setting import SettingsScreen
from product import ProductScreen

Builder.load_file(os.path.join("kv", "home.kv"))
Builder.load_file(os.path.join("kv", "product.kv"))
Builder.load_file(os.path.join("kv", "cart.kv"))


kivy.require("2.3.0")

class ShopPalApp(App):
    def build(self):
        return Builder.load_file('main.kv')
    
    def switch_screen_slide(self, screen_name, dir, dur=.5):
        sm = self.root
        sm.transition = SlideTransition(
            direction=dir, 
            duration=dur
        )
        sm.current = screen_name
        print("sliding", dir)
    


if __name__ == '__main__':
    ShopPalApp().run()
