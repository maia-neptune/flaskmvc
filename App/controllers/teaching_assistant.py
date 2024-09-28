from App.database import db
from App.models.teaching_assistant import *


def create_teaching_assistant(prefix, firstName, lastName, faculty):

    teachingAssistant = TeachingAssistant(prefix = prefix, firstName = firstName, lastName = lastName, faculty = faculty)
    db.session.add(teachingAssistant)
    db.session.commit()

    return teachingAssistant

def get_teachingAssistant(id):

    teachingAssistant = TeachingAssistant.query.filter_by(id=id).first()

    if teachingAssistant:
        return teachingAssistant
    
    return None

def fire_teaching_assistant(id):

    teachingAssistant = TeachingAssistant.query.filter_by(id = id).first()

    if teachingAssistant:
        db.session.delete(teachingAssistant)
        db.session.commit()
    
