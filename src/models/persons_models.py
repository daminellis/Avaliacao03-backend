from database.db import db
class Log(db.Model):
    __tablename__ = 'persons'

    # Definição das colunas
    Persons_id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    Last_Name = db.Column(db.Varchar(255), nullable=False)
    First_Name = db.Column(db.Varchar(255), nullable=False)
    Age = db.Column(db.Integer, nullable=False)

    # Método para retornar um dicionário com os dados
    def to_dict(self):
        return {
            'Persons_id': self.Persons_id,
            'Last_Name': self.Last_Name,
            'First_Name': self.First_Name,
            'Age': self.Age,
            'tabela': 'persons' 
        }
