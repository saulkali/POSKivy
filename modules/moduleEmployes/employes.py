from cgitb import text
import string
from kivymd.uix.card import MDCard
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFillRoundFlatIconButton,MDRoundFlatIconButton

from kivy.clock import Clock

from pydantic import ValidationError

from common.database.firebase import employes
from common.entities.employe_entity import EmployeEntity
from common.values import strings

from .adapters.employesAux import EmployesAux

from modules.moduleDetailsEmploye.detailsEmploye import DetailsEmploye


class EmployesMDCard(MDCard,EmployesAux):
    dialog:MDDialog = None
    listEmployes:list = []

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(lambda *args: self.getEmployes())

    def getEmployes(self):
        self.ids.recycle_view_employes.data = []
        self.listEmployes = employes.getAllEmployes()
        for employe in self.listEmployes:
            self.addItemRecycleView(employe)
    
    def filterEmployes(self):
        self.ids.recycle_view_employes.data = []
        rfcField = self.ids.text_field_search_employe.text.__str__()
        if rfcField.__len__() != 0:
            for employe in self.listEmployes:
                if rfcField in employe.firstName or rfcField in employe.lastName or rfcField in employe.rfc:
                    self.addItemRecycleView(employe)
            self.clearFields()
        else:
            self.getEmployes()
    
    def setFocusField(self,field,*args):
        field.focus = True

    def clearFields(self):
        self.ids.text_field_search_employe.text = ""
        
        Clock.schedule_once(lambda *args: self.setFocusField(self.ids.text_field_search_employe,*args))
    def addItemRecycleView(self,employe:EmployeEntity):
        self.ids.recycle_view_employes.data.append(
            {
                "listener":self,
                "employe": employe,
                "photoUrl": employe.photoUrl,
                "text": f"{employe.firstName} {employe.lastName}",
                "secondary_text": employe.rfc,
                "tertiary_text": employe.permissions.__str__()
            }
        )
    
    
    def dialogClose(self,*args):
        if self.dialog is not None:
            self.dialog.dismiss(force=True)

    def validateEmploye(self,*args):
        try:
            employe = EmployeEntity(
                photoUrl = self.dialog.content_cls.ids.text_field_photo_url.text,
                rfc = self.dialog.content_cls.ids.text_field_rfc.text,
                firstName = self.dialog.content_cls.ids.text_field_first_name.text,
                lastName = self.dialog.content_cls.ids.text_field_last_name.text,
                password =self.dialog.content_cls.ids.text_field_password.text,
                phone = self.dialog.content_cls.ids.text_field_phone.text,
                address = self.dialog.content_cls.ids.text_field_address.text,
                email = self.dialog.content_cls.ids.text_field_email.text
            )
            if self.dialog.content_cls.isEdit:
                if employes.updateEmploye(employe):
                    Snackbar(text = strings.msg_success_update_employe).open()
                else:
                    Snackbar(text = strings.msg_error_update_employe).open()
            else:
                if employes.saveEmploye(employe):
                    Snackbar(text = strings.msg_success_save_employe).open()
                else:
                    Snackbar(text = strings.error)
            self.dialogClose()
            self.getEmployes()
        except ValidationError as error:
            pass


    def addEmploye(self):
        detailsEmploye = DetailsEmploye()
        self.dialog = MDDialog(
            title = strings.title_create_employe,
            type = "custom",
            content_cls = detailsEmploye,
            buttons = [
                MDRoundFlatIconButton(
                    icon = "exit-run",
                    text = "Cancelar",
                    on_press = self.dialogClose
                ),
                MDFillRoundFlatIconButton(
                    icon = "content-save-all",
                    text = "Guardar",
                    on_press = self.validateEmploye
                )
            ]
            )
        self.dialog.open()


    ################
    ##Employe Aux
    ################
    def deleteEmploye(self,employe:EmployeEntity):
        if employes.deleteEmploye(employe):
            Snackbar(text = strings.msg_success_delete_employe).open()
            self.getEmployes()
        else:
            Snackbar(text= strings.msg_error_delete_employe).open()
    def editEmploye(self,employe:EmployeEntity):
        detailsEmploye = DetailsEmploye(employe = employe )
        self.dialog = MDDialog(
            title = strings.title_edit_employe,
            type = "custom",
            content_cls = detailsEmploye,
            buttons = [
                MDRoundFlatIconButton(
                    icon = "exit-run",
                    text = "Cancelar",
                    on_press = self.dialogClose
                ),
                MDFillRoundFlatIconButton(
                    icon = "content-save-all",
                    text = "Guardar",
                    on_press = self.validateEmploye
                )
            ]
            )
        self.dialog.open()