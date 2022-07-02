from cgitb import text
from tkinter import dialog
from turtle import title
from kivymd.uix.card import MDCard
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.clock import Clock
from pydantic import ValidationError

from modules.moduleDetailsArticle.detailsArticle import DetailsArticleScreen


from common.entities.article_entity import ArticleEntity
from common.database.firebase import articles
from common.values import strings
class InventoryMDCard(MDCard):

    def __init__(self, **kw) -> None:
        super(InventoryMDCard,self).__init__(**kw)
        Clock.schedule_once(lambda *kargs:self.getArticles())
        

    def getArticles(self):
        self.ids.recycle_view_articles.data = [
            {
                "article":article
            } for article in articles.getAllArticles()]
    
    def filterArticles(self):
        self.ids.recycle_view_articles.data = []
        codeBar = self.ids.text_field_code_bar.text.__str__()
        if codeBar.__len__() > 0:
            listFilterArticle:list = []
            for article in articles.getAllArticles():
                if codeBar in article.id  or codeBar in article.name:
                    listFilterArticle.append(article)
            print(listFilterArticle)
            self.ids.recycle_view_articles.data = [
            {
                "article":article
            } for article in listFilterArticle]
        else:
            dialog = MDDialog(text = strings.msg_code_bar_search_is_empty)
            dialog.open()

    def addArticle(self):
        detailsArticle = DetailsArticleScreen()
        self.dialog = MDDialog(
            title = strings.title_create_article,
            type = "custom",
            content_cls = detailsArticle,
            buttons = [
                MDFlatButton(
                    text = "Cancelar",
                    on_press = self.dialogClose
                ),
                MDFlatButton(
                    text = "Guardar",
                    on_press = self.validateArticle
                )
            ]
            )
        self.dialog.open()
    def dialogClose(self, *args):
        self.dialog.dismiss(force=True)

    def validateArticle(self,*args):
        try:
            articleEntity = ArticleEntity(
                id = self.dialog.content_cls.ids.text_field_code_bar.text,
                name = self.dialog.content_cls.ids.text_field_name.text,
                description = self.dialog.content_cls.ids.text_field_description.text,
                photoUrl = self.dialog.content_cls.ids.text_field_photo_url.text,
                price = float (self.dialog.content_cls.ids.text_field_price.text),
                amount = float(self.dialog.content_cls.ids.text_field_amount.text),
                offSale = float(self.dialog.content_cls.ids.text_field_off_sale.text),
                shelf = self.dialog.content_cls.ids.text_field_shelf.text,
                vertical = self.dialog.content_cls.ids.text_field_vertical.text,
                horizontal = self.dialog.content_cls.ids.text_field_horizontal.text,
                category = self.dialog.content_cls.ids.drop_down_item_category.text
            )
            '''if self.isEdit:
                articles.updateArticle(articleEntity)
                self.listener.reloadInventory.emit()
                self.close()
            else:'''
            if articles.existsArticle(articleEntity.id):
                dialog = MDDialog(title = strings.msg_error,text = strings.msg_article_exists)
                dialog.open()
            else:
                articles.saveArticle(articleEntity)
                self.getArticles()
            self.dialogClose()

        except ValidationError as error:
            dialog = MDDialog(title = strings.msg_error,text = error.errors.__str__())
            dialog.open()
    