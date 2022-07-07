from kivymd.uix.card import MDCard
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFillRoundFlatIconButton,MDRoundFlatIconButton
from kivymd.uix.snackbar import Snackbar
from kivy.clock import Clock
from pydantic import ValidationError

from modules.moduleDetailsArticle.detailsArticle import DetailsArticleScreen


from common.entities.article_entity import ArticleEntity
from common.database.firebase import articles
from common.values import strings

class InventoryMDCard(MDCard):
    listArticle: articles = articles
    def __init__(self, **kw) -> None:
        super(InventoryMDCard,self).__init__(**kw)
        Clock.schedule_once(lambda *kargs:self.getArticles())
        
    def open_card(self):
        print("card open")

    def addItemRecycleView(self,article:ArticleEntity):
        self.ids.recycle_view_articles.data.append({
                "listener":self,
                "article":article,
                "codeBar":article.id,
                "photoUrl":article.photoUrl,
                "name":article.name,
                "amount":article.amount.__str__(),
                "price":article.price.__str__()
            }
        )
    def getArticles(self):
        self.ids.recycle_view_articles.data = []
        self.listArticle = articles.getAllArticles()
 
        for article in self.listArticle:
            self.addItemRecycleView(article)
        
    
    def filterArticles(self):
        self.ids.recycle_view_articles.data = []
        codeBar = self.ids.text_field_code_bar.text.__str__()
        if codeBar.__len__() > 0:
            listFilterArticle:list = []
            for article in articles.getAllArticles():
                if codeBar in article.id  or codeBar in article.name:
                    listFilterArticle.append(article)
            for article in listFilterArticle:
                self.addItemRecycleView(article)            
            self.ids.recycle_view_articles.refresh_from_data()
            self.ids.recycle_view_articles.refresh_from_layout()
        else:
            '''dialog = MDDialog(text = strings.msg_code_bar_search_is_empty)
            dialog.open()'''
            self.getArticles()
        

    def addArticle(self):
        detailsArticle = DetailsArticleScreen()
        self.dialog = MDDialog(
            title = strings.title_create_article,
            type = "custom",
            content_cls = detailsArticle,
            buttons = [
                MDRoundFlatIconButton(
                    icon = "exit-run",
                    text = "Cancelar",
                    on_press = self.dialogClose
                ),
                MDFillRoundFlatIconButton(
                    icon = "content-save-all",
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
            if self.dialog.content_cls.isEdit == True:
                self.updateArticleInventory(articleEntity)
                self.getArticles()
            else:
                if articles.existsArticle(articleEntity.id):
                    dialog = MDDialog(title = strings.msg_error,text = strings.msg_article_exists)
                    dialog.open()
                else:
                    articles.saveArticle(articleEntity)
                    self.getArticles()
                    Snackbar(text=strings.msg_save_success_article).open()
            self.dialogClose()

        except ValidationError as error:
            dialog = MDDialog(title = strings.msg_error,text = error.errors.__str__())
            dialog.open()
    





    ####################
    ## InventoryAux
    ####################
    def deleteArticleInventory(self,article:ArticleEntity):
        print("delete article firebase", article.id)
        if articles.deleteArticle(article):
            Snackbar(text=strings.msg_success_delete_article).open()
            self.getArticles()
        else:
            Snackbar(text=strings.msg_error_delete_article).open()

    def updateArticleInventory(self,article:ArticleEntity):
        if articles.updateArticle(article):
            Snackbar(text=strings.msg_success_update_article).open()
        else:
            Snackbar(text=strings.msg_error_delete_article).open()
    
    def openEditArticle(self,article:ArticleEntity):
        detailsArticle = DetailsArticleScreen(article)
        self.dialog = MDDialog(
            title = strings.title_create_article,
            type = "custom",
            content_cls = detailsArticle,
            buttons = [
                MDRoundFlatIconButton(
                    icon = "exit-run",
                    text = "Cancelar",
                    on_press = self.dialogClose
                ),
                MDFillRoundFlatIconButton(
                    icon = "content-save-all",
                    text = "Guardar",
                    on_press = self.validateArticle
                )
            ]
            )
        self.dialog.open()