from kivymd.uix.card import MDCard
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from common.entities.shopping_car_entity import ShoppingCardEntity

class CardShoppingWidget(MDCard):
    def __init__(self,shopping:ShoppingCardEntity,**kygs) -> None:
        super(MDCard,self).__init__(**kygs)
        self.shopping = shopping
        self.setupShopping()

        
    def setupShopping(self):
        self.ids.image_article.source = self.shopping.photoUrlArticle
        self.ids.label_name.text = self.shopping.nameArticle
        self.ids.text_field_amount = self.shopping.amountArticle.__str__()
    
    
    def delete(self):
        dialog = MDDialog(text="¿delea eleminar?",buttons = [
            MDFlatButton(text="Si"),
            MDFlatButton(text ="No")
        ])
        dialog.open()
