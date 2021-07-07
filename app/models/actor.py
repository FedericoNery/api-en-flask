from app.db import db, BaseModelMixin


class Actor(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    film_id = db.Column(db.Integer, db.ForeignKey('film.id'), nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Actor({self.name})'

    def __str__(self):
        return f'{self.name}'