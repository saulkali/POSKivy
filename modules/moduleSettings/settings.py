from kivymd.uix.screen import MDScreen
from kivy.lang.builder import Builder
from helper import getFile

Builder.load_file(getFile("modules/moduleSettings/settings.kv"))

class SettingsScreen(MDScreen):
    def __init__(self, **kw):
        super().__init__(**kw)
    
    def openMainScreen(self):
        self.manager.current = "mainScreen"