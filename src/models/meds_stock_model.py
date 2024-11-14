from database.db import db
class MedStock(db.Model):
    __tablename__ = 'med_stock'

    # Definição das colunas
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    med_name = db.Column(db.Varchar(100), nullable=False)
    med_qtd = db.Column(db.Integer, nullable=False)
    med_val = db.Column(db.Date, nullable=False)
    med_desc = db.Column(db.Text)
    med_type = db.Column(db.Enum('comprimido', 'xarope', 'injeção', 'pomada'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    # Método para retornar um dicionário com os dados
    def to_dict(self):
        return {
            'id': self.id,
            'med_name': self.med_name,
            'med_qtd': self.med_qtd,
            'med_val': self.med_val,
            'med_desc': self.med_desc,
            'med_type': self.med_type,
            'user_id': self.user_id,
            'tabela': 'med_stock'
        }
