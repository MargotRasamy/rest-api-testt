from pydantic import BaseModel

class ModelPersonne(BaseModel):
    nom: str
    prenom: str
    ssn: str
