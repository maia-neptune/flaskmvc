from App.database import db
from .staff import Staff

class Lecturer(Staff):
    __tablename__ = 'lecturer'
    id = db.Column(db.Integer, db.ForeignKey('staff.id'), primary_key= True)


    def __init__(self, prefix, firstName, lastName, faculty):
        super().__init__(prefix, firstName, lastName, faculty, 'Lecturer')