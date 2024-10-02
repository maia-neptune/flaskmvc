from App.database import db
from .staff import Staff

class TeachingAssistant(Staff):
    __tablename__ = 'teaching_assistant'
    id = db.Column(db.Integer, db.ForeignKey('staff.id'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity': 'teaching_assistant',
    }

    def __init__(self, username, password, prefix, firstName, lastName, faculty):
        super().__init__(username, password, prefix, firstName, lastName, faculty, 'Teaching Assistant')