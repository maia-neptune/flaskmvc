from App.database import db
from App.models.lecturer import *

def create_lecturer(prefix, firstName, lastName, faculty):

    lecturer = Lecturer(prefix = prefix, firstName = firstName, lastName = lastName, faculty = faculty)
    db.session.add(lecturer)
    db.session.commit()

    return lecturer


def get_lecturer(id):
    
    lecturer = Lecturer.query.filter_by(id = id).first()

    if lecturer:
        return lecturer
    
    return None


def fire_lecturer(id):

    lecturer = Lecturer.query.filter_by(id = id).first()

    if lecturer:
        db.session.delete(lecturer)
        db.session.commit()

def validate_prefix(prefix):
    return prefix in ['Mrs.', 'Dr.', 'Mr.', 'Ms.', 'Prof.']


def validate_faculty(faculty):
    return faculty in ['FOE', 'FST', 'FSS', 'FMS', 'FHE', 'FOL', 'FFA', 'FOS']


def create_and_confirm_lecturer(prefix, firstName, lastName, faculty):
    if not validate_prefix(prefix):
        return "Invalid prefix. Use: Prof., Dr., Mrs., Mr., or Ms."

    if not validate_faculty(faculty):
        return "Invalid faculty. Use: FOE, FST, FSS, FMS, FHE, FOL, FFA, or FOS"

    lecturer = create_lecturer(prefix, firstName, lastName, faculty)
    return f'Lecturer created: {lecturer.prefix} {lecturer.firstName} {lecturer.lastName}. ID: {lecturer.id}'