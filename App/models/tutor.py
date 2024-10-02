from App.database import db
from .staff import Staff


class Tutor(Staff):
    __tablename__ = 'tutor'
    id = db.Column(db.Integer, db.ForeignKey('staff.id'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity': 'tutor',
    }

    def __init__(self, username, password, prefix, firstName, lastName, faculty):
        super().__init__(username, password, prefix, firstName, lastName, faculty, 'Tutor')


