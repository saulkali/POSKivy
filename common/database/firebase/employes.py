from common.firebase.firebase import FireBase

from common.entities.employe_entity import EmployeEntity
from common.firebase import constants as firebaseConstants


firebase = FireBase()

def saveEmploye(employeEntity:EmployeEntity)->bool:
    '''create new employe firebase'''
    try:
        firebase.db.child(firebaseConstants.referenceEmploye).child(employeEntity.rfc).set(employeEntity.dict())
        return True
    except:
        return False
def updateEmploye(employeEntity:EmployeEntity)->bool:
    print(employeEntity)
    firebase.db.child(firebaseConstants.referenceEmploye).child(employeEntity.rfc).update(employeEntity.dict())
    return True


def deleteEmploye(employeEntity:EmployeEntity)->bool:
    try:
        firebase.db.child(firebaseConstants.referenceEmploye).child(employeEntity.rfc).delete()
        return True
    except:
        return False

def getAllEmployes() -> list:
    '''get all employes firebase'''
    listEmployes = []
    employesJson = firebase.db.child(firebaseConstants.referenceEmploye).get()
    if employesJson != None:
        for key,value in employesJson.items():
            employeEntity = EmployeEntity.parse_obj(value)
            listEmployes.append(employeEntity)
    return listEmployes

def loginEmploye(email:str,password:str)->bool:
    employeJson = firebase.db.child(firebaseConstants.referenceEmploye).order_by_child("email").equal_to(email).limit_to_first(1).get().popitem()
    if employeJson is not None:
        key,value = employeJson
        employeEntity = EmployeEntity.parse_obj(value)
        if employeEntity.password.__eq__(password):
            return True
        return False
    return False