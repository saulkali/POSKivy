from kivymd.uix.card import MDCard
from kivy.lang import Builder

from common.widgets.cardClientWidget.cardClient import CardClientWidget
class ClientsMDCard(MDCard):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)