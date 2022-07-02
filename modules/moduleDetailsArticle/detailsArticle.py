from kivymd.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from common.entities.article_entity import ArticleEntity
from common.values import strings

class DetailsArticleScreen(BoxLayout):

    article:ArticleEntity

    def __init__(self, article:ArticleEntity = None,**kw):
        super().__init__(**kw)
        self.article = article