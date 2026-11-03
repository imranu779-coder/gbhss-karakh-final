from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
import json, os

SCHOOL = "GOVT BOYS HSS KARAKH"
DIST = "DIST. KHUZDAR - BALOCHISTAN"
THEME = [0.06, 0.36, 0.18, 1]
DATA_FILE = "students.json"

class GBHSSApp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', spacing=8, padding=15, **kwargs)
        
        self.add_widget(Label(text=SCHOOL, font_size=18, bold=True, color=THEME, size_hint_y=None, height=35))
        self.add_widget(Label(text=DIST, font_size=13, size_hint_y=None, height=20))
        
        # Tabs
        tabs = BoxLayout(size_hint_y=None, height=45, spacing=5)
        self.btn_form = Button(text="ADD STUDENT", background_color=THEME)
        self.btn_list = Button(text="STUDENT LIST", background_color=[0.3,0.3,0.3,1])
        tabs.add_widget(self.btn_form); tabs.add_widget(self.btn_list)
        self.add_widget(tabs)
        
        self.form_box = BoxLayout(orientation='vertical', spacing=6)
        self.list_box = BoxLayout(orientation='vertical', spacing=6)
        
        # --- FORM ---
        self.t_name = TextInput(hint_text="Bache ka Naam", multiline=False, size_hint_y=None, height=42)
        self.t_fname = TextInput(hint_text="Walid ka Naam", multiline=False, size_hint_y=None, height=42)
        self.t_class = TextInput(hint_text="Class (e.g 10th)", multiline=False, size_hint_y=None, height=42)
        self.t_roll = TextInput(hint_text="Roll No", multiline=False, size_hint_y=None, height=42)
        
        dob_label = Label(text="Date of Birth:", bold=True, size_hint_y=None, height=25)
        dob_row = BoxLayout(spacing=5, size_hint_y=None, height=42)
        self.t_dd = TextInput(hint_text="Din", input_filter='int')
        self.t_mm = TextInput(hint_text="Mahina", input_filter='int')
        self.t_yy = TextInput(hint_text="Saal", input_filter='int')
        dob_row.add_widget(self.t_dd); dob_row.add_widget(self.t_mm); dob_row.add_widget(self.t_yy)
        
        self.t_contact = TextInput(hint_text="Contact Number", multiline=False, size_hint_y=None, height=42)
        
        for w in [self.t_name, self.t_fname, self.t_class, self.t_roll, dob_label, dob_row, self.t_contact]:
            self.form_box.add_widget(w)
        
        save_btn = Button(text="SAVE STUDENT", background_color=THEME, size_hint_y=None, height=50, bold=True)
        save_btn.bind(on_press=self.save_data)
        self.form_box.add_widget(save_btn)
        self.msg = Label(text="", size_hint_y=None, height=30, color=THEME)
        self.form_box.add_widget(self.msg)
        
        # --- LIST ---
        self.search = TextInput(hint_text="Search naam se...", size_hint_y=None, height=42)
        self.search.bind(text=self.refresh_list)
        self.list_box.add_widget(self.search)
        self.scroll = ScrollView()
        self.grid = GridLayout(cols=1, spacing=5, size_hint_y=None)
        self.grid.bind(minimum_height=self.grid.setter('height'))
        self.scroll.add_widget(self.grid)
        self.list_box.add_widget(self.scroll)
        
        self.container = BoxLayout()
        self.container.add_widget(self.form_box)
        self.add_widget(self.container)
        
        self.btn_form.bind(on_press=self.show_form)
        self.btn_list.bind(on_press=self.show_list)
        
        self.load_data()
    
    def show_form(self, *args):
        self.btn_form.background_color = THEME
        self.btn_list.background_color = [0.3,0.3,0.3,1]
        self.container.clear_widgets()
        self.container.add_widget(self.form_box)
    def show_list(self, *args):
        self.btn_list.background_color = THEME
        self.btn_form.background_color = [0.3,0.3,0.3,1]
        self.container.clear_widgets()
        self.container.add_widget(self.list_box)
        self.refresh_list()
    
    def load_data(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r') as f:
                self.data = json.load(f)
        else:
            self.data = []
    
    def save_data(self, *args):
        if not self.t_name.text or not self.t_yy.text:
            self.msg.text = "Naam aur Saal lazmi hai!"
            return
        rec = {
            "name": self.t_name.text,
            "fname": self.t_fname.text,
            "class": self.t_class.text,
            "roll": self.t_roll.text,
            "dob": f"{self.t_dd.text}/{self.t_mm.text}/{self.t_yy.text}",
            "contact": self.t_contact.text
        }
        self.data.append(rec)
        with open(DATA_FILE, 'w') as f:
            json.dump(self.data, f)
        self.msg.text = f"{rec['name']} Save Ho Gaya!"
        self.t_name.text = self.t_fname.text = self.t_class.text = self.t_roll.text = self.t_contact.text = self.t_dd.text = self.t_mm.text = self.t_yy.text = ""
    
    def refresh_list(self, *args):
        self.grid.clear_widgets()
        q = self.search.text.lower()
        for i, s in enumerate(self.data):
            if q in s['name'].lower():
                txt = f"{s['name']} | {s['class']} | Roll:{s['roll']} | DOB:{s['dob']} | F:{s['fname']}"
                self.grid.add_widget(Label(text=txt, size_hint_y=None, height=35, font_size=12))

class MainApp(App):
    def build(self):
        return GBHSSApp()

MainApp().run()