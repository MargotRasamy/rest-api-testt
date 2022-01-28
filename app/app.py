from fastapi import FastAPI, HTTPException
from db import database
from model_personne import ModelPersonne

app = FastAPI()
db = database()

# [GET] personnes
@app.get("/personnes")
def get_personnes():
    results = db.personnes.find()
    personnes = []
    for result in results:
        personnes.append({ "nom": result["nom"], "prenom": result["prenom"], "ssn": result["ssn"] })
    return personnes

# [POST] personnes
@app.post("/personnes")
def create_personne(personneAInserer : ModelPersonne):
    if db.personnes.find_one({"ssn":personneAInserer.ssn}) is not None:
        HTTPException(status=404, detail="Ssn de cette personne existe deja")
    db.personnes.insert_one(personneAInserer.dict())
    return f'Vous avez inseré {personneAInserer.dict()} !'

# [GET] personnes/ssn
@app.get("/personnes/{myssn}")
def get_personne(myssn: str):
    result = db.personnes.find_one({"ssn": myssn})
    if db.personnes.find_one({"ssn": myssn}) is not None:
        HTTPException(status=404, detail=f'People with ssn {myssn} are not found')
    return {"nom": result["nom"], "prenom": result["prenom"], "ssn": result["ssn"]}
    

# [DELETE] personnes/ssn
# [GET] personnes/ssn
@app.delete("/personnes/{myssn}")
def delete_personne(myssn: str):
    result = db.personnes.delete_one({ "ssn": myssn})
    personne = {"nom": result["nom"], "prenom": result["prenom"], "ssn": result["ssn"]}
    return f'Deleted person {personne}'


# [UPDATE] personnes/ssn

