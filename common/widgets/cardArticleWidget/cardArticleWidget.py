from kivymd.uix.card import MDCard
from kivy.clock import Clock
from kivymd.uix.dialog import MDDialog
from kivy.properties import ObjectProperty,StringProperty

from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from common.values import strings

class CardArticleWidget(MDCard):
    dialog:MDDialog = None

    listener = ObjectProperty(None)
    article = ObjectProperty(None)
    codeBar = StringProperty()
    photoUrl = StringProperty()
    name = StringProperty()
    amount = StringProperty()
    price = StringProperty()

    def __init__(self,**kygs) -> None:
        super().__init__(**kygs)
        self.setupTextField()
    
    def setFocusPrice(self,instance,focus):
        if focus == False:
            self.setPrice(self.ids.text_field_price.text)

    def setFocusAmount(self,instance,focus):
        if focus == False:
            self.setAmount(self.ids.text_field_amount.text)
    
    def setupTextField(self):
        self.ids.text_field_price.bind(focus = self.setFocusPrice)
        self.ids.text_field_amount.bind(focus = self.setFocusAmount)
    
    def deleteArticle(self,*args):
        self.listener.deleteArticleInventory(self.article)
        self.closeDialog()

    def closeDialog(self,*args):
        if self.dialog is not None:
            self.dialog.dismiss(force=True)

    def confirmDeleteArticle(self):
        self.dialog = MDDialog(title=strings.msg_delete_ask,buttons = [
            MDFlatButton(text=strings.btn_no,on_press = self.closeDialog),
            MDFlatButton(text =strings.btn_yes,on_press= self.deleteArticle)
        ])
        self.dialog.open()

    def confirmUpdateArticle(self):
        self.dialog = MDDialog(
            title = strings.msg_ask_update_change,
            buttons = [
                MDFlatButton(
                    text = strings.btn_no,
                    on_press = self.closeDialog
                ),
                MDFlatButton(
                    text = strings.btn_yes,
                    on_press = self.update
                )
            ]
        )
        self.dialog.open()

    def update(self,*args):
        self.article.amount =float(self.ids.text_field_amount.text) 
        self.article.price = float(self.ids.text_field_price.text)
        self.listener.updateArticleInventory(self.article)
        self.ids.text_field_price.error = False
        self.ids.text_field_amount.error = False
        
        self.ids.text_field_price.text = self.article.price.__str__()
        self.ids.text_field_amount.text = self.article.amount.__str__()
        self.closeDialog()
    
    def seeMore(self):
        self.listener.openEditArticle(self.article)
    
    def setAmount(self,value:str):
        print(f"amount:{value} {self.article.name}")
        if value.__len__() == 0:
            value = "0"
            self.ids.text_field_amount.text = value
        if value.__eq__(self.article.amount.__str__()):
            self.ids.text_field_amount.error = False
        else:
            self.ids.text_field_amount.error = True

    def setPrice(self,value:str):
        print("Price: ",value)
        if value.__len__() == 0:
            value = "0"
            self.ids.text_field_price.text = value
        if value.__eq__(self.article.price.__str__()):
            self.ids.text_field_price.error = False
        else:
            self.ids.text_field_price.error = True