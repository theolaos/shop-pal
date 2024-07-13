from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label


def add_entry(bl):
    fl = FloatLayout()

    # add label left
    _lbl = Label()
    _lbl.id = '_lbl0'
    _lbl.text = 'LEFT'
    _lbl.size_hint_x = 0.3
    _lbl.pos_hint = {'x': 0, 'center_y': .5}
    fl.add_widget(_lbl)

    # add label center
    _lbl1 = Label()
    _lbl1.id = '_lbl1'
    _lbl1.text = 'CENTER'
    _lbl1.size_hint_x = 0.3
    _lbl1.pos_hint = {'center_x': .5, 'center_y': .5}
    fl.add_widget(_lbl1)

    # add label right
    _lbl2 = Label()
    _lbl2.id = '_lbl2'
    _lbl2.text = 'RIGHT'
    _lbl2.size_hint_x = 0.3
    _lbl2.pos_hint = {'right': 1, 'center_y': .5}
    fl.add_widget(_lbl2)

    bl.add_widget(fl)


class MyApp(App):

    def build(self):
        bl = BoxLayout()
        bl.orientation = 'vertical'
        for g in range(3):
            add_entry(bl)
        return bl

if __name__ == '__main__':
    MyApp().run()