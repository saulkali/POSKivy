from kivymd.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.properties import BooleanProperty
from common.entities.article_entity import ArticleEntity
from common.values import strings



class DetailsArticleScreen(BoxLayout):

    article:ArticleEntity
    isEdit = BooleanProperty(False)
    def __init__(self, article:ArticleEntity = None,**kw):
        super().__init__(**kw)
        self.article = article
        self.setupArticle()

    def setupArticle(self):
        if self.article is not None:
            self.isEdit = True
            self.ids.image_photo.source = self.article.photoUrl
            self.ids.text_field_photo_url.text = self.article.photoUrl
            self.ids.text_field_code_bar.text = self.article.id
            self.ids.text_field_code_bar_confirm.text = self.article.id
            self.ids.text_field_name.text = self.article.name
            self.ids.text_field_description.text = self.article.description
            self.ids.text_field_amount.text = self.article.amount.__str__()
            self.ids.text_field_price.text = self.article.price.__str__()
            self.ids.text_field_off_sale.text = self.article.offSale.__str__()
            self.ids.text_field_shelf.text = self.article.shelf
            self.ids.text_field_vertical.text = self.article.vertical
            self.ids.text_field_horizontal.text = self.article.horizontal