from database.db import db
class Notebook(db.Model):
    __tablename__ = 'notebook'

    # Definição das colunas
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    note_title = db.Column(db.Varchar(100), nullable=False)
    med_stock_id = db.Column(db.Integer, db.ForeignKey('med_stock.id'), nullable=False)
    note_desc = db.Column(db.Text)
    med_method = db.Column(db.Enum('diário', 'controlado'), default=None)
    med_type = db.Column(db.Enum('comprimido', 'xarope', 'injeção', 'pomada'), default=None)
    med_freq = db.Column(db.Varchar(50), nullable=False)
    qtd_taken = db.Column(db.Integer, nullable=False)
    qtd_total = db.Column(db.Integer, nullable=False)
    init_schedule = db.Column(db.DateTime, nullable=False)
    end_schedule = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.Enum('ativo', 'completo', 'cancelado'), default='ativo')
    obs = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    # Método para retornar um dicionário com os dados
    def to_dict(self):
        return {
            'id': self.id,
            'note_title': self.note_title,
            'med_stock_id': self.med_stock_id,
            'note_desc': self.note_desc,
            'med_method': self.med_method,
            'med_type': self.med_type,
            'med_freq': self.med_freq,
            'qtd_taken': self.qtd_taken,
            'qtd_total': self.qtd_total,
            'init_schedule': self.init_schedule,
            'end_schedule': self.end_schedule,
            'status': self.status,
            'obs': self.obs,
            'user_id': self.user_id,
            'tabela': 'notebook'
        }
