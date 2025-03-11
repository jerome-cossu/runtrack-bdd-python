import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

class Employe:
    def __init__(self, id=None, nom=None, prenom=None, salaire=None, id_service=None):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.salaire = salaire
        self.id_service = id_service
    
    def connect():
        mot_de_passe = os.getenv("MOT_DE_PASSE")
        return mysql.connector.connect(
            host="127.0.0.1",
    user="root",
    password=mot_de_passe,
    database="LaPlateforme"
        )
    
    def create(self):
        connection = Employe.connect()
        cursor = connection.cursor()
        query = "UPDATE employe SET nom = %s, prenom = %s, salaire = %s, id_service = %s WHERE id = %s"
        cursor.execute(query, (self.nom, self.prenom, self.salaire, self.id_service, self.id))
        connection.commit()
        cursor.close()
        connection.close()

    def read_all():
        connection = Employe.connect()
        cursor = connection.cursor()
        query = "SELECT e.id, e.nom, e.prenom, e.salaire, s.nom AS service FROM employe e JOIN service s ON e.id_service = s.id"
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            print(f"ID: {row[0]}, Nom: {row[1]}, Prénom: {row[2]}, Salaire: {row[3]}, Service: {row[4]}")
        cursor.close()
        connection.close()
    
    def read_high_salary():
        connection = Employe.connect()
        cursor = connection.cursor()
        query = "SELECT * FROM employe WHERE salaire > 3000"
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            print(f"ID: {row[0]}, Nom: {row[1]}, Prénom: {row[2]}, Salaire: {row[3]}, ID Service: {row[4]}")
        cursor.close()
        connection.close()

    def update(self):
        connection = Employe.connect()
        cursor = connection.cursor()
        query = "UPDATE employe SET nom = %s, prenom = %s, salaire = %s, id_service = %s WHERE id = %s"
        cursor.execute(query, (self.nom, self.prenom, self.salaire, self.id_service, self.id))
        connection.commit()
        cursor.close()
        connection.close()

    def delete(self):
        connection = Employe.connect()
        cursor = connection.cursor()
        query = "DELETE FROM employe WHERE id = %s"
        cursor.execute(query, (self.id,))
        connection.commit()
        cursor.close()
        connection.close()
    
emp = Employe(nom="Doe", prenom="John", salaire=4000, id_service=1)
emp.create()

print("Liste des employés :")
Employe.read_all()

print("\nListe des employés gagnant plus de 3000€ :")
Employe.read_high_salary()

emp.id = 1
emp.nom = "Doe"
emp.prenom = "John"
emp.salaire = 3600
emp.update()

emp_to_delete = Employe(id=2)
emp_to_delete.delete()