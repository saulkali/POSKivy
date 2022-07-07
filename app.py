#kivy
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager

#modules
from modules.moduleMain.main import MainScreen
from helper import getFile

class ManagerScreens(ScreenManager):
    def __init__(self):
        super().__init__()
        self.setupScreens()

    def setupScreens(self):
        shoppingCarScreen = MainScreen(name="mainScreen")
        self.add_widget(shoppingCarScreen)
        

Builder.load_file(getFile("common/widgets/cardShoppingWidget/cardShoppingWidget.kv"))

Builder.load_file(getFile("modules/moduleMain/main.kv"))
Builder.load_file(getFile("modules/moduleDetailsArticle/detailsArticle.kv"))

Builder.load_file(getFile("modules/moduleShoppingCar/widgets/mount.kv"))


class MainApp(MDApp):
    def build(self):
        #self.theme_cls.theme_style = "Dark"
        return ManagerScreens()

if __name__ == "__main__":
    MainApp().run()