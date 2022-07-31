from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from helper import getFile

Builder.load_file(getFile("modules/moduleLogin/login.kv"))

class LoginScreen(MDScreen):
    def __init__(self, **kw):
        super().__init__(**kw)