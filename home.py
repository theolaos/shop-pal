from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.metrics import dp


class ProductButton(BoxLayout):
    def __init__(self, height=dp(100), **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.size_hint_y = None
        self.height = height

        self.add_widget(Button(text="img",size_hint=(1,3)))
        self.add_widget(Label(text="info",size_hint=(1,1.25)))
        self.add_widget(Button(text="Add to cart"))

class Products(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.spacing = [10, 10]  # Horizontal and vertical spacing
        self.padding = 10
        self.size_hint_y = None
        self.w, self.h = dp(110),dp(110)
        self.bind(minimum_height=self.setter('height'))

        for i in range(1, 26):
            self.add_widget(ProductButton(size_hint_y=None, height=self.h))

        # Add the "Add more products" button
        self.add_widget(Button(text="Add more products", size_hint_y=1, height=self.h))

        # Bind the size change to adjust columns dynamically
        Window.bind(on_resize=self.update_columns_width)
        self.update_columns_width(Window, Window.width, Window.height)

    def update_columns_width(self, instance, width, height):
        # Calculate the number of columns based on the window width
        product_width = self.w + self.spacing[0]  # Product width + horizontal spacing
        cols = max(1, int(width / product_width))
        self.cols = cols

class Home(BoxLayout): 
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"

        header = BoxLayout(size_hint=(1, 0.1))
        header.add_widget(
            Button(
                text="Settings", 
                on_press=self.switch_screen( 
                    'settings',
                    SlideTransition(
                        direction="right",
                        duration=.5
                    )
                )
            )
        )
        header.add_widget(Label(text="ShopPal"))
        header.add_widget(
            Button(
                text="Cart", 
                on_press=self.switch_screen( 
                    'cart',
                    SlideTransition(
                        direction="left",
                        duration=.5
                    )
                )
            )
        )
        self.add_widget(header)

        scroll_view = ScrollView(size_hint=(1, 0.9))
        products = Products()
        scroll_view.add_widget(products)
        self.add_widget(scroll_view)
    
    def switch_screen(self, screen_name, transition):
        def switch(*args):
            app = App.get_running_app()
            app.root.transition = transition
            app.root.current = screen_name
        return switch

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Home())
