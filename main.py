from os.path import join as join_path
from kivy import require as kivy_require

import kivymd

from kivy.uix.screenmanager import SlideTransition
from kivymd.app import MDApp
from kivy.lang import Builder

from src.home import HomeScreen
from src.cart import CartScreen
from src.setting import SettingsScreen
from src.product import ProductScreen

Builder.load_file(join_path("src", "kv", "home.kv"))
Builder.load_file(join_path("src", "kv", "product.kv"))
Builder.load_file(join_path("src", "kv", "cart.kv"))
Builder.load_file(join_path("src", "kv", "setting.kv"))


kivy_require("2.3.0")

class ShopPalApp(MDApp):
    def build(self):
        return Builder.load_file('main.kv')
    
    def switch_screen_slide(self, screen_name, dir, dur=.5):
        sm = self.root
        sm.transition = SlideTransition(
            direction=dir, 
            duration=dur
        )
        sm.current = screen_name


if __name__ == '__main__':
    ShopPalApp().run()
