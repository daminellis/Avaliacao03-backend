from database.db import db
class Log(db.Model):
    __tablename__ = 'notebook'

    # Definição das colunas
    Notebook_Id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    Note_Title = db.Column(db.Varchar(255))
    Med_Name = db.Column(db.Varchar(255))
    Med_Desc = db.Column(db.Text)
    Med_Method = db.Column(db.Enum('diário','controlado'))
    Med_Type = db.Column(db.Enum('comprimido','xarope','injeção','pomada'))
    Med_Freq = db.Column(db.Varchar(50))
    Qtd_Taken = db.Column(db.Integer)
    Qtd_Total = db.Column(db.Integer)
    Init_Schedule = db.Column(db.DateTime)
    End_Schedule = db.Column(db.DateTime)
    status = db.Column(db.Enum('ativo','completo','cancelado'))
    Obs = db.Column(db.Text)
    Person_Id = db.Column(db.Integer, db.ForeignKey('persons.Person_id'))
    
    def to_dict(self):
        return {
            'Notebook_Id': self.Notebook_Id,
            'Note_Title': self.Note_Title,
            'Med_Name': self.Med_Name,
            'Med_Desc': self.Med_Desc,
            'Med_Method': self.Med_Method,
            'Med_Type': self.Med_Type,
            'Med_Freq': self.Med_Freq,
            'Qtd_Taken': self.Qtd_Taken,
            'Qtd_Total': self.Qtd_Total,
            'Init_Schedule': self.Init_Schedule,
            'End_Schedule': self.End_Schedule,
            'status': self.status,
            'Obs': self.Obs,
            'Person_Id': self.Person_Id,
            'tabela': 'notebook' 
        }
