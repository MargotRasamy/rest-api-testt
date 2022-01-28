
from pymongo import MongoClient

class MongoSeeder:

    def __init__(self) -> None:
        client = MongoClient(host="mongodb")
        self.mydb = client.registre

    @property
    def db(self):
        return self.mydb

    def seed_db(self):
        self.db.create_collection("personnes")
        
        self.db.personnes.insert_one({ "prenom" : "Margot", "nom": "Rasamy", "ssn": "432432432432" })

        self.db.personnes.insert_one({ "prenom" : "Hello", "nom": "Kitty", "ssn": "432332432432" })

print("Filling DB")
MongoSeeder().seed_db()
        