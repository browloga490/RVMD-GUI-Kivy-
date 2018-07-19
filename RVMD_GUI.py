import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.widget import Widget
from kivy.core.window import Window

from kivy.config import Config
Config.set('graphics', 'width', '1024')
Config.set('graphics', 'height', '600')
Config.write()
#Window.size = (1024, 600)

class ScreenOne(Screen):
    pass

class ScreenTwo(Screen):
    pass

class Channel_1(ScreenManager):
    pass

class Channel_2(ScreenManager):
    pass

class Channel_3(ScreenManager):
    pass

class Channel_4(ScreenManager):
    pass

class CalcGridLayout(GridLayout):
    pass

class OptGridLayout(GridLayout):
    pass

class Test(TabbedPanel):

    tab_pos = 'top_mid'
    tab_width = Window.width / 4
  

presentation = Builder.load_file("main.kv")


        
class MainApp(App):
    
    def build(self):
        return presentation

if __name__ == "__main__":
    MainApp().run()

