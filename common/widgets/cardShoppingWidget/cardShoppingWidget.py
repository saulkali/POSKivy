from kivymd.uix.card import MDCard
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from common.entities.shopping_car_entity import ShoppingCardEntity
from modules.moduleShoppingCar.adapter.shoppingAux import ShoppingAux

class CardShoppingWidget(MDCard):
    
    shopping:ShoppingCardEntity
    listener:ShoppingAux

    def __init__(self,shopping:ShoppingCardEntity,listener:ShoppingAux,**kygs) -> None:
        super(MDCard,self).__init__(**kygs)
        self.shopping = shopping
        self.listener = listener
        self.setupShopping()

        
    def setupShopping(self):
        self.ids.image_article.source = self.shopping.photoUrlArticle
        self.ids.label_name.text = self.shopping.nameArticle
        self.ids.text_field_amount.text = self.shopping.amountArticle.__str__()
        self.ids.label_price.text = self.shopping.priceUniArticle.__str__()
        self.ids.label_total.text = f"Total -> ${self.getTotal()}"

    def removeItem(self):
        self.listener.removeItemShoppingCar(self)

    def confirmRemove(self):
        dialog = MDDialog(text="¿delea eleminar?",buttons = [
            MDFlatButton(text="No"),
            MDFlatButton(
                text ="Si",
                on_press = self.removeItem
                )
        ])
        dialog.open()

    def enterAmount(self,value):
        if value.__len__() == 0:
            self.ids.text_field_amount.text = "1"
            self.shopping.amountArticle = 1
        else:
            self.ids.text_field_amount.text = value
            self.shopping.amountArticle = float(value)
        self.setupShopping()
        self.listener.setTotalShoppingCar()

    def getTotal(self)->float:
        return self.shopping.priceUniArticle * self.shopping.amountArticle