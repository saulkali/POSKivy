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
        self.listener.updateArticleInventory(self.article)
        self.closeDialog()
    
    def seeMore(self):
        self.listener.openEditArticle(self.article)
