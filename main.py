"""
Example on how to use ScrollView 

bar_width - sets the width of the scrollbar
bar_margin - sets the margin between the widget and the button
scroll_type - determines whether to scroll content or sidebar
scroll_type: ["bars"]  # scrollbar only
scroll_type: ["content"] # scroll content only
scroll_type: ["bars", "content"] # both
"""


from kivymd.app import MDApp
from kivy.lang import Builder

import os

text = ""
with open("longtext.txt", "r") as fp:
    text = fp.read()


if os.name == 'nt':
    scroll_type = ["bars"]
else:
    scroll_type = ["content"]

KV = f'''
MDBoxLayout:
    orientation: "vertical"
    ScrollView:
        size_hint: 1, 1
        scroll_type: {scroll_type}
        bar_width: "20dp"
        id: sv
        MDGridLayout:
            cols: 1
            adaptive_height: True
            spacing: "10dp"
            padding: "10dp"
            MDBoxLayout:
                adaptive_height: True
                MDLabel:
                    font_style: "Overline"
                    text: "Overline label"
                    id: label
                    size_hint_y: None
                    height: self.texture_size[1]
'''

class MainApp(MDApp):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.primary_palette = "Teal"    
    
    def on_start(self):
        self.root.ids.label.text = text
    
    def build(self):
        return Builder.load_string(KV)

MainApp().run()