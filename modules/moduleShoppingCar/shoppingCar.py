from kivymd.uix.card import MDCard
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from common.database.firebase import articles

from common.widgets.cardShoppingWidget.cardShoppingWidget import CardShoppingWidget
from common.entities.shopping_car_entity import ShoppingCardEntity
from common.values import strings

class ShoppingCarMDCard(MDCard):
    def __init__(self,**kargs) -> None:
        super().__init__(**kargs)
    
    def addArticleShoppingCar(self,cardArticle:CardShoppingWidget):
        self.ids.shopping_car_container.add_widget(cardArticle)
    
    def clearFields(self):
        self.ids.text_field_code_bar.text = ""
        self.ids.text_field_code_bar.focus = True
        
    def searchArticle(self,codeBar:str):
        if codeBar.__len__() > 0:
            if articles.existsArticle(codeBar):
                article = articles.getArticleById(codeBar)
                shoppingEntity = ShoppingCardEntity(
                    idArticle = article.id,
                    photoUrlArticle = article.photoUrl,
                    nameArticle = article.name,
                    amountArticle = 1.0,
                    priceUniArticle = article.price)
                cardShopping = CardShoppingWidget(shoppingEntity)
                self.addArticleShoppingCar(cardShopping)
            else:
                dialog = MDDialog(title = strings.msg_article_not_found)
                dialog.open()
            self.clearFields()
        else:
            dialog = MDDialog(title = strings.msg_code_bar_search_is_empty)
            dialog.open()

    def clearShoppingCar(self):
        print("clear shopping car")