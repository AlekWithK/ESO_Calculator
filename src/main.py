from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.core.window import Window
from kivy.uix.textinput import TextInput


Window.clearcolor = (.21,.21,.21,1) #Button header color
Builder.load_file('ui.kv')

class Frame(TabbedPanel):
        pass

class ESOCalc(App):
    def build(self):
        self.title = 'ESO Calculators'
        self.icon = 'Resources/eso.png'
        return Frame()

if __name__ == "__main__":
    ESOCalc().run()