import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.widget import Widget
from kivy.core.window import Window


class MainScreen(Screen):
    pass

class AnotherScreen(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass

class CalcGridLayout(GridLayout):
    pass

class OptGridLayout(GridLayout):
    pass

class Test(TabbedPanel):

    tab_pos = 'top_mid'
    tab_width = Window.width / 2

presentation = Builder.load_file("main.kv")

        
class MainApp(App):
    
    def build(self):
        return presentation

if __name__ == "__main__":
    MainApp().run()

