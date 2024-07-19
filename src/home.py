from kivy.uix.screenmanager import Screen
from kivy.metrics import dp
from kivymd.uix.card import MDCard
from kivy.uix.recycleview import RecycleView



class ProductButton(MDCard):
    def __init__(self, height=dp(100), **kwargs):
        super().__init__(**kwargs)
        self.height = height # styling stuff


class ProductRecycleView(RecycleView):
    def __init__(self, **kwargs):
        super(ProductRecycleView, self).__init__(**kwargs)
        
        self.data = [
            {'product_img': f'assets/banana.png', 'product_name': f'Banana {i}'}
            for i in range(100)
        ]


class HomeScreen(Screen): 
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # ProductRecycleView()