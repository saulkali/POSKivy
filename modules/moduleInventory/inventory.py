from kivymd.uix.card import MDCard
from kivy.clock import Clock
from kivy.properties import ListProperty
from common.widgets.cardArticleWidget.cardArticleWidget import CardArticleWidget
from common.database.firebase import articles

class InventoryMDCard(MDCard):

    listArticles:list = []

    def __init__(self, **kw) -> None:
        super(InventoryMDCard,self).__init__(**kw)
        Clock.schedule_once(lambda *kargs:self.getArticles())
        

    def getArticles(self):
        listArticles = articles.getAllArticles()
        self.ids.recycle_view_articles.data = [
            {
                "article":article
            } for article in listArticles]
            