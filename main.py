from kivymd.uix.pickers import MDTimePicker
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivy.uix.widget import Widget
from kivymd.app import MDApp


Window.size = (360, 800)

KV = '''
MDFloatLayout:

    MDRaisedButton:
        text: "Open time picker"
        pos_hint:{"center_x": .5, "center_y": .6}
        on_release: app.show_time_picker()
    MDLabel:
        id: select_time
        text: "тут время"
        halign: "center"
        
'''

class testA(FloatLayout):
    pass
class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def show_time_picker(self):
        '''Open time picker dialog.'''
        time_dialog = MDTimePicker()
        # a = testA()
        time_dialog.bind(on_save=self.on_save, on_cancel = self.on_cancel)
        time_dialog.open()
    def on_save(self, intence, value):
        self.root.ids.select_time.text = str(value)
    def on_cancel(self, intence, value):
        self.root.ids.select_time.text = "Отменено"

if __name__ == "__main__":
    Test().run()