
from kivymd.uix.screen import MDScreen


from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

from common.database.firebase import articles

from common.widgets.cardArticleWidget.cardArticleWidget import CardArticleWidget


class MainScreen(MDScreen):
    def __init__(self):
        super().__init__()

    def searchArticle(self,codeBar:str):
        print(codeBar)
        if articles.existsArticle(codeBar):
            article = articles.getArticleById(codeBar)
            cardArticle = CardArticleWidget(article)
            self.addArticleShoppingCar(cardArticle)
        else:
            dialog = MDDialog(text = "Articulo No encontrado")
            dialog.open()
        self.clearFields()