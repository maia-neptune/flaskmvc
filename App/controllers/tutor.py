from App.database import db
from App.models.tutor import *

def create_tutor(prefix, firstName, lastName, faculty):

    tutor = Tutor(prefix = prefix, firstName = firstName, lastName = lastName, faculty = faculty)
    db.session.add(tutor)
    db.session.commit()

    return tutor

def get_tutor(id):
    tutor = Tutor.query.filter_by(id = id).first()

    if tutor:
        return tutor
    
    return None

def fire_tutor(id):

    tutor = Tutor.query.filter_by(id = id).first()

    if tutor:
        db.session.delete(tutor)
        db.session.commit()
    
