from database.db import db
class Log(db.Model):
    __tablename__ = 'meds_stock'

    # Definição das colunas
    Meds_Name = db.Column(db.Varchar(200))
    Meds_Qtd = db.Column(db.Integer, nullable=False)
    Meds_val = db.Column(db.Date, nullable=False)
    Required_Person = db.Column(db.Integer, db.ForeignKey('persons.Person_id'))
    Meds_Stock_Id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    Meds_Desc = db.Column(db.Text)
    Meds_Type = db.Column(db.Enum('comprimido','xarope','injeção','pomada'))

    # Método para retornar um dicionário com os dados
    def to_dict(self):
        return {
            'Meds_Name': self.Meds_Name,
            'Meds_Quantity': self.Meds_Qtd,
            'Meds_val': self.Meds_val,
            'Required_Person': self.Required_Person,
            'Meds_Stock_Id': self.Meds_Stock_Id,
            'Meds_Desc': self.Meds_Desc,
            'Meds_Type': self.Meds_Type,
            'tabela': 'meds_stock' 
        }

