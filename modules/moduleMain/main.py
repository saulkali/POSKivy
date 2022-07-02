from kivymd.uix.screen import MDScreen
from common.widgets.cardArticleWidget.cardArticleWidget import CardArticleWidget


class MainScreen(MDScreen):
    def __init__(self,**kargs):
        super().__init__(**kargs)
    
    def clearShoppingCar(self):
        print("clear shopping car")