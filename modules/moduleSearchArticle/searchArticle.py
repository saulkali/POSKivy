from kivy.uix.boxlayout import BoxLayout

from.adapter.searchArticleAux import SearchArticleAux
from kivy.clock import Clock
from common.database.firebase import articles


from common.entities.article_entity import ArticleEntity

class SearchArticle(BoxLayout,SearchArticleAux):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.loadArticle)
        
    def addArticle(self,article:ArticleEntity):
        print("add article shopping card")

    def loadArticle(self,*args):
        listArticle = articles.getAllArticles()
        for article in listArticle:
            self.addItemRecycleView(article)

    def addItemRecycleView(self,article:ArticleEntity):
        self.ids.recycle_view_search_articles.data.append({
                "listener":self,
                "article": article,
                "text":article.name,
                "secondary_text":article.price,
                "tertiary_text": f"estante: {article.shelf}, vertical: {article.vertical}, horizontal: {article.horizontal}"
            }
        )