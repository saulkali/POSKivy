from http import client
from common.firebase.firebase import FireBase
from common.entities.client_entity import ClientEntity
from common.firebase import constants


firebase = FireBase()

def getAllClients()->list[ClientEntity]:
    listClient = []
    jsonClient = firebase.db.child(constants.referenceClients).get()
    if jsonClient is not None:
        for key,value in jsonClient.items():
            clientEntity = ClientEntity.parse_obj(value)
            clientEntity.id = key.__str__()
            listClient.append(clientEntity)
    return listClient

def saveClient(client:ClientEntity)-> ClientEntity:
    key = firebase.db.child(constants.referenceClients).push().key.__str__()
    client.id = key
    firebase.db.child(constants.referenceClients).child(key).set(client.dict())
    return client