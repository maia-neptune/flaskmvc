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

def validate_prefix(prefix):
    return prefix in ['Mrs.', 'Dr.', 'Mr.', 'Ms.', 'Prof.']

def validate_faculty(faculty):
    return faculty in ['FOE', 'FST', 'FSS', 'FMS', 'FHE', 'FOL', 'FFA', 'FOS']

def create_and_confirm_tutor(prefix, firstName, lastName, faculty):
    if not validate_prefix(prefix):
        return "Invalid prefix. Use: Prof., Dr., Mrs., Mr., or Ms."

    if not validate_faculty(faculty):
        return "Invalid faculty. Use: FOE, FST, FSS, FMS, FHE, FOL, FFA, or FOS"

    tutor = create_tutor(prefix, firstName, lastName, faculty)
    return f'Tutor created: {tutor.prefix} {tutor.firstName} {tutor.lastName}. ID: {tutor.id}'

    
