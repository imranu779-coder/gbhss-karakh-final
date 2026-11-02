from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivy.core.window import Window
Window.softinput_mode = "below_target"

KV = '''
MDScreen:
    md_bg_color: 0.95, 0.95, 0.95, 1
    
    MDBoxLayout:
        orientation: "vertical"
        padding: "20dp"
        spacing: "20dp"
        pos_hint: {"center_x": .5, "center_y": .5}
        size_hint: .9, .8
        
        MDLabel:
            text: "GBHSS KARKH"
            halign: "center"
            font_style: "H5"
            bold: True
            theme_text_color: "Custom"
            text_color: 0, 0.4, 0.2, 1
            size_hint_y: None
            height: "50dp"
            
        MDLabel:
            text: "Govt. Boys Higher Secondary School\\nKarkh District Khuzdar\\nBalochistan"
            halign: "center"
            theme_text_color: "Secondary"
            size_hint_y: None
            height: "80dp"
            
        MDBoxLayout:
            orientation: "vertical"
            spacing: "15dp"
            adaptive_height: True
            
            MDRaisedButton:
                text: "STUDENT ADMISSION"
                pos_hint: {"center_x": .5}
                size_hint_x: .9
                md_bg_color: 0, 0.5, 0.3, 1
                on_release: app.show_msg("Admission Module")
                
            MDRaisedButton:
                text: "STUDENT RECORD"
                pos_hint: {"center_x": .5}
                size_hint_x: .9
                md_bg_color: 0, 0.4, 0.8, 1
                on_release: app.show_msg("Student Record")
                
            MDRaisedButton:
                text: "ATTENDANCE"
                pos_hint: {"center_x": .5}
                size_hint_x: .9
                md_bg_color: 0.8, 0.4, 0, 1
                on_release: app.show_msg("Attendance System")
                
            MDRaisedButton:
                text: "FEES RECORD"
                pos_hint: {"center_x": .5}
                size_hint_x: .9
                md_bg_color: 0.6, 0.2, 0.8, 1
                on_release: app.show_msg("Fees Module")
                
            MDRaisedButton:
                text: "STAFF RECORD"
                pos_hint: {"center_x": .5}
                size_hint_x: .9
                md_bg_color: 0.8, 0, 0.2, 1
                on_release: app.show_msg("Staff Record")
                
        MDLabel:
            text: "Developed for GBHSS Karkh\\nPrincipal: Sohail Ahmed"
            halign: "center"
            theme_text_color: "Hint"
            font_style: "Caption"
'''

class GBHSSApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        return Builder.load_string(KV)
    
   