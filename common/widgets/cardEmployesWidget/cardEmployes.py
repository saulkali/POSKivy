from turtle import title
from kivymd.uix.list import ThreeLineAvatarIconListItem
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.properties import StringProperty,ObjectProperty


from modules.moduleEmployes.adapters.employesAux import EmployesAux
from common.values import strings

class CardEmployesWidget(ThreeLineAvatarIconListItem):
    listener = ObjectProperty(None)
    photoUrl = StringProperty()
    employe = ObjectProperty(None)

    dialog:MDDialog = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def confirmDeleteEmploye(self):
        self.dialog = MDDialog(
            title = strings.msg_delete_ask,
            buttons = [
                MDFlatButton(
                    text = strings.btn_no,
                    on_press = self.closeDialog
                ),
                MDFlatButton(
                    text= strings.btn_yes,
                    on_press = self.deleteEmploye
                )
            ]
        )
        self.dialog.open()

    def openEditEmploye(self):
        self.listener.editEmploye(self.employe)
    
    def closeDialog(self,*args):
        if self.dialog is not None:
            self.dialog.dismiss(force=True)

    def deleteEmploye(self,*args):
        self.listener.deleteEmploye(self.employe)
        self.closeDialog()



