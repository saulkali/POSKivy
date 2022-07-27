from kivymd.uix.list import ThreeLineAvatarIconListItem
from kivy.properties import StringProperty
class CardArticleSearchWidget(ThreeLineAvatarIconListItem):
    photoUrl = StringProperty()
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)