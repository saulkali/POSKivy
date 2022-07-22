from pydantic import BaseModel
from datetime import datetime

class ClientEntity(BaseModel):
    id:str = ""
    rfc:str = ""
    photoUrl:str = ""
    firstName:str = ""
    lastName:str = ""
    email:str = ""
    cp:int = 0
    phone:str = ""
    dateTime:str = datetime.now().__str__()
    address:str = ""
    city:str = ""
    listArticles = str
