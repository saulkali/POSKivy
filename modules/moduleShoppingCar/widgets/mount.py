from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.dialog import MDDialog
from modules.moduleShoppingCar.adapter.shoppingAux import ShoppingAux
class MountPay(BoxLayout):
    listener:ShoppingAux

    def __init__(self,listener:ShoppingAux, **kwargs):
        super(MountPay,self).__init__(**kwargs)
        self.listener = listener

    def setMount(self,value:str):
        if value.__len__() > 0:
            if float(value) < self.listener.getTotal():
                self.ids.text_field_mount.error = True
            else:
                self.listener.finishShoppingCar(float(value))   