from kivymd.app import App
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivymd.uix.boxlayout import BoxLayout

import os

text = ""
with open("longtext.txt", "r") as fp:
    text = fp.read()

KV = f'''
MyBoxLayout:
    scrollview: root.ids.sv
    orientation: "vertical"
    ScrollView:
        scroll_type: ["bars"]
        id: sv
        MDLabel:
            text: {text}
            id: label
            size_hint:
            size: self.texture_size
'''

class MyBoxLayout(BoxLayout):
    
    scrollview = ObjectProperty("")

class MainApp(App):
    
    def build(self):
        return Builder.load_string(KV)

MainApp().run()