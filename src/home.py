from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, SlideTransition, SwapTransition
from kivy.metrics import dp
from kivymd.uix.imagelist import MDSmartTile
from kivymd.uix.card import MDCard
from kivymd.uix.recyclegridlayout import RecycleGridLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior



class ProductButton(MDCard):
    def __init__(self, height=dp(100), **kwargs):
        super().__init__(**kwargs)
        self.height = height # styling stuff


class ProductView(RecycleDataViewBehavior, GridLayout):
    def refresh_view_attrs(self, rv, index, data):
        """ Catch and handle the view changes """
        self.ids.product_image.source = data['source']
        self.ids.product_name.text = data['name']
        return super(ProductView, self).refresh_view_attrs(rv, index, data)


class ProductRecycleView(RecycleView):
    def __init__(self, **kwargs):
        super(ProductRecycleView, self).__init__(**kwargs)
        self.data = [
            {'source': f'path_to_image_{i}.jpg', 'name': f'Product {i}'}
            for i in range(100)
        ]


class Products(RecycleGridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.spacing = [10, 10]  # Horizontal and vertical spacing
        self.padding = 10
        self.size_hint_y = None
        self.w, self.h = dp(110),dp(110)
        self.bind(minimum_height=self.setter('height'))

        for i in range(1, 26):
            self.add_widget(ProductButton(size_hint_y=None, height=self.h))

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
    #     self.add_widget(Home())
