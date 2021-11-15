from kivy.config import Config
Config.set('graphics', 'resizable', False)

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.clock import Clock

from funcs import normalizer

Window.size = (500, 500)
Window.clearcolor = (.21,.21,.21,1) #Button header color
Builder.load_file('ui.kv')

class Frame(TabbedPanel):
    def __init__(self, **kwargs):
        super(Frame, self).__init__(**kwargs)
    
    def button_pressed(self):
        t_dps = int(self.ids.t_dps.text)
        self.ids.result_lbl.text = f'Result: {t_dps}'
        self.ids.t_dps.text = ''        
        pass

class ESOCalc(App):
    def build(self):
        self.title = 'ESO Calculators'
        self.icon = 'Resources/eso.png'
        return Frame()   
        

if __name__ == "__main__":
    ESOCalc().run()