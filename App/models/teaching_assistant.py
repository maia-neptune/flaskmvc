from App.database import db
from .staff import Staff

class TeachingAssistant(Staff):
    __tablename__ = 'teaching_assistant'
    id = db.Column(db.Integer, db.ForeignKey('staff.id'), primary_key= True)


    def __init__(self, prefix, firstName, lastName, faculty):
        super().__init__(prefix, firstName, lastName, faculty, 'Teaching Assistant')

