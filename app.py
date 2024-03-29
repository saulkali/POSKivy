#kivy
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.lang.builder import Builder
from helper import getFile
#modules
from modules.moduleMain.main import MainScreen
from modules.moduleSettings.settings import SettingsScreen
from modules.moduleLogin.login import LoginScreen

class ManagerScreens(ScreenManager):
    def __init__(self):
        super().__init__()
        self.setupScreens()

    def setupScreens(self):
        loginScreen = LoginScreen(name="loginScreen")
        shoppingCarScreen = MainScreen(name="mainScreen")
        settingsScreen = SettingsScreen(name="settingsScreen")
        
        self.add_widget(loginScreen)
        self.add_widget(shoppingCarScreen)
        self.add_widget(settingsScreen)



class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return ManagerScreens()

if __name__ == "__main__":
    MainApp().run()