from kivy.uix.boxlayout import BoxLayout
from kivy.properties import BooleanProperty

from common.entities.employe_entity import EmployeEntity
from modules.moduleEmployes.adapters.employesAux import EmployesAux

class DetailsEmploye(BoxLayout):
    employe:EmployeEntity
    isEdit = BooleanProperty(False)
    
    def __init__(self,employe:EmployeEntity = None,**kwargs):
        super().__init__(**kwargs)
        self.employe = employe
        self.loadEmploye()

    def loadEmploye(self):
        if self.employe is not None:
            self.isEdit = True
            self.ids.text_field_photo_url.text = self.employe.photoUrl
            self.ids.text_field_rfc.text = self.employe.rfc
            self.ids.text_field_first_name.text = self.employe.firstName
            self.ids.text_field_last_name.text = self.employe.lastName
            self.ids.text_field_password.text = self.employe.password
            self.ids.text_field_confirm_password.text = self.employe.password
            self.ids.text_field_phone.text = self.employe.phone
            self.ids.text_field_address.text = self.employe.address
            self.ids.text_field_email.text = self.employe.email 
            
    