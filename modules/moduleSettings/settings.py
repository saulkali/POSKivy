from kivymd.uix.screen import MDScreen
from kivy.lang.builder import Builder
from kivy.clock import Clock
from helper import getFile
from common.settings.settings_manager import SettingsManager
from common.utils.printer import PrinterEscPos
from common.values import array_string

Builder.load_file(getFile("modules/moduleSettings/settings.kv"))

class SettingsScreen(MDScreen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.loadSettings()
        Clock.schedule_once(lambda *args: self.setupDropDownItem())
    def openMainScreen(self):
        self.manager.current = "mainScreen"
    
    def setupDropDownItem(self):
        self.ids.drop_down_item_printer_type.items = [item for item in array_string.listTypePrinter]

    def loadSettings(self):
        self.ids.text_field_usb_printer.text = SettingsManager().printer.usbPort


    def saveSettigns(self):
        SettingsManager().printer.usbPort = self.ids.text_field_usb_printer.text 
    
        SettingsManager().save()
    
    def searchUsbPort(self):
        PrinterEscPos().scanPortPrinter()
        self.ids.text_field_usb_printer.text = PrinterEscPos().DEV
