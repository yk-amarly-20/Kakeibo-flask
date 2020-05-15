from flask_kakeibo import db
from datetime import datetime


class Entry(db.Model):
    __tablename__ = 'entries'
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50))
    outcome = db.Column(db.Integer)
    memo = db.Column(db.String(50))
    created_at = db.Column(db.DateTime)
    
    # データを受け取り, テーブルに追加する
    def __init__(self, category=None, outcome=None, memo=None):
        self.category = category
        self.outcome = outcome
        self.memo = memo
        self.created_at = datetime.utcnow()

    def __repr__(self):
        return '<Entry id:{0} category:{1} outcome:{2} memo:{3}>'.format(self.id, self.category, self.outcome, self.memo)
