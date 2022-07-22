from kivymd.uix.screen import MDScreen
from kivy.lang.builder import Builder
from kivy.clock import Clock
from helper import getFile
from common.settings.settings_manager import SettingsManager

Builder.load_file(getFile("modules/moduleSettings/settings.kv"))

class SettingsScreen(MDScreen):
    def __init__(self, **kw):
        super().__init__(**kw)
        Clock.schedule_once(lambda *args:self.loadSettings())

    def openMainScreen(self):
        self.manager.current = "mainScreen"
    
    def loadSettings(self):
        self.ids.text_field_usb_printer.text = SettingsManager().printer.dev

