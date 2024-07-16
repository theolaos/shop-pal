from kivy.app import App

def switch_screen(self, screen_name, transition):
    def switch(*args):
        self.manager.transition = transition
        self.manager.current = screen_name
    return switch


def switch_screen_root(screen_name, transition):
    def switch(*args):
        app = App.get_running_app()
        app.root.transition = transition
        app.root.current = screen_name
    return switch

class Cart:
    ITEMS = []