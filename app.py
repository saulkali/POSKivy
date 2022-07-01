#kivy
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager

#modules
from modules.moduleMain.main import MainScreen

from helper import getFile

Builder.load_file(getFile("modules/moduleMain/main.kv"))
Builder.load_file(getFile("common/widgets/cardArticleWidget/cardArticleWidget.kv"))
Builder.load_file(getFile("common/widgets/cardShoppingWidget/cardShoppingWidget.kv"))
class ManagerScreens(ScreenManager):
    def __init__(self):
        super().__init__()
        self.setupScreens()

    def setupScreens(self):
        shoppingCarScreen = MainScreen()
        self.add_widget(shoppingCarScreen)
        

class MainApp(MDApp):
    def build(self):
        #self.theme_cls.theme_style = "Dark"
        return ManagerScreens()

if __name__ == "__main__":
    MainApp().run()