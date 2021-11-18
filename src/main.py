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

#Worker functions
from funcs import normalizer, calc_avg_crit, calc_max_crit

Window.size = (500, 650)
Window.clearcolor = (.21,.21,.21,0) #Button header color
Builder.load_file('ui.kv')
class Frame(TabbedPanel):
    def __init__(self, **kwargs):
        super(Frame, self).__init__(**kwargs)
    
    def normalizer_pressed(self):
        try:
            t_dps = int(self.ids.t_dps.text)
            c_chance = float(self.ids.c_chance.text)
            t_hits = int(self.ids.t_hits.text)
            t_c_hits = int(self.ids.t_c_hits.text)
            t_non_hits = int(self.ids.t_non_hits.text)
            c_damage = float(self.ids.c_damage.text)
            
            result, delta = normalizer(t_dps, c_chance, t_hits, t_c_hits, t_non_hits, c_damage)
            self.ids.result_lbl.text = f"Result: {result}\nChange: {delta}"
        except:
            self.ids.result_lbl.text = f'Please check \n your inputs!'  
    
    #src = textinput ID | src2 = label ID        
    def checkbox_click(self, instance, val, src, src2):
        avg_crit = round(calc_avg_crit(self, src, src2, val), 2)
        max_crit = round(calc_max_crit(self, src, val), 2)
        self.ids.crit_result.text = f"Average Crit Damage: {avg_crit}%\nMaximum Crit Damage: {max_crit}%"
        return    
class ESOCalc(App):
    def build(self):
        self.title = 'ESO Utility v1.0'
        self.icon = 'Resources/icon.png'
        return Frame()       

if __name__ == "__main__":
    ESOCalc().run()