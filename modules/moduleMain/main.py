from kivymd.uix.screen import MDScreen
from kivy.lang.builder import Builder

from helper import getFile

from common.widgets.cardArticleWidget.cardArticleWidget import CardArticleWidget
from modules.moduleShoppingCar.shoppingCar import ShoppingCarMDCard
from modules.moduleInventory.inventory import InventoryMDCard
Builder.load_file(getFile("modules/moduleMain/main.kv"))
Builder.load_file(getFile("common/widgets/cardShoppingWidget/cardShoppingWidget.kv"))
Builder.load_file(getFile("modules/moduleDetailsArticle/detailsArticle.kv"))
Builder.load_file(getFile("modules/moduleDetailsEmploye/detailsEmploye.kv"))
Builder.load_file(getFile("modules/moduleShoppingCar/widgets/mount.kv"))

class MainScreen(MDScreen):
    def __init__(self,**kargs):
        super().__init__(**kargs)
    
    def openSettingsScreen(self):
        self.manager.current = "settingsScreen"
        
    
   