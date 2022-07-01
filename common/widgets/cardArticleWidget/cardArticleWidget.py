from kivymd.uix.card import MDCard
from kivy.clock import Clock
from kivy.properties import ObjectProperty
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from common.values import strings


class CardArticleWidget(MDCard):
    article = ObjectProperty(None)
    def __init__(self,**kygs) -> None:
        super(MDCard,self).__init__(**kygs)
        Clock.schedule_once(lambda *args: self.loadArticle())
    def delete(self):
        dialog = MDDialog(text=strings.msg_delete_ask,buttons = [
            MDFlatButton(text=strings.btn_no),
            MDFlatButton(text =strings.btn_yes)
        ])
        dialog.open()
    def loadArticle(self):
        self.ids.image_article.source = self.article.photoUrl
        self.ids.label_name.text = self.article.name
    def update(self):
        print("update")
    def seeMore(self):
        print(self.article)
