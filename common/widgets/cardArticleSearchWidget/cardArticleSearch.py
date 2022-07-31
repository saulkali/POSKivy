from kivymd.uix.list import ThreeLineAvatarIconListItem
from kivy.properties import StringProperty,ObjectProperty
class CardArticleSearchWidget(ThreeLineAvatarIconListItem):
    photoUrl = StringProperty()
    article = ObjectProperty()
    listener = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def addArticle(self):
        if self.article is not None:
            self.listener.addArticle(self.article)