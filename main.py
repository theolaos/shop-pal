import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.label import Label

kivy.require("2.3.0")

class ProductButton(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.size_hint = (None, None)
        self.size = (150, 150)

        self.add_widget(Label(text="img"))
        self.add_widget(Label(text="info"))
        self.add_widget(Button(text="Add to cart"))

class Products(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'lr-tb'
        self.padding = 10
        self.spacing = 10
        self.size_hint_y = None
        self.bind(minimum_height=self.setter('height'))

        for i in range(1, 26):
            self.add_widget(ProductButton())

class Menu(BoxLayout): 
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"

        header = BoxLayout(size_hint=(1, 0.1))
        header.add_widget(Button(text="Settings"))
        header.add_widget(Label(text="ShopPal"))
        header.add_widget(Button(text="Cart"))
        self.add_widget(header)

        scroll_view = ScrollView(size_hint=(1, 0.9))
        products = Products()
        scroll_view.add_widget(products)
        self.add_widget(scroll_view)

class ShopPalApp(App):
    def build(self):
        return Menu()

if __name__ == '__main__':
    ShopPalApp().run()
