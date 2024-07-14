import kivy

from kivy.uix.screenmanager import ScreenManager
from kivy.app import App

from home import HomeScreen
from cart import CartScreen
from setting import SettingsScreen

kivy.require("2.3.0")

class ShopPalApp(App):
    def build(self):
        screen_manager = ScreenManager()

        screen_manager.add_widget(HomeScreen(name='home'))
        screen_manager.add_widget(CartScreen(name='cart'))
        screen_manager.add_widget(SettingsScreen(name='settings'))

        return screen_manager

if __name__ == '__main__':
    ShopPalApp().run()
