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

def validate_prefix(prefix):
    return prefix in ['Mrs.', 'Dr.', 'Mr.', 'Ms.', 'Prof.']

def validate_faculty(faculty):
    return faculty in ['FOE', 'FST', 'FSS', 'FMS', 'FHE', 'FOL', 'FFA', 'FOS']

def create_and_confirm_ta(prefix, firstName, lastName, faculty):
    if not validate_prefix(prefix):
        return "Invalid prefix. Use: Prof., Dr., Mrs., Mr., or Ms."

    if not validate_faculty(faculty):
        return "Invalid faculty. Use: FOE, FST, FSS, FMS, FHE, FOL, FFA, or FOS"

    ta = create_teaching_assistant(prefix, firstName, lastName, faculty)
    return f'Teaching Assistant created: {ta.prefix} {ta.firstName} {ta.lastName}. ID: {ta.id}'

    
