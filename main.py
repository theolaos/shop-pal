import kivy

from kivy.uix.screenmanager import ScreenManager, SlideTransition
from kivy.app import App

from home import HomeScreen
from cart import CartScreen
from setting import SettingsScreen
from product import ProductScreen

kivy.require("2.3.0")

class ShopPalApp(App):
    def build(self):
        screen_manager = ScreenManager()

        screen_manager.add_widget(HomeScreen(name='home'))
        screen_manager.add_widget(CartScreen(name='cart'))
        screen_manager.add_widget(SettingsScreen(name='settings'))
        screen_manager.add_widget(ProductScreen(name='product'))

        return screen_manager
    
    def switch_screen_slide(self, screen_name, dir, dur):
        sm = self.root
        def switch(*args):
            self.manager.transition = SlideTransition(
                direction=dir, 
                duration=dur
            )
            sm.current = screen_name
        return switch


if __name__ == '__main__':
    ShopPalApp().run()
