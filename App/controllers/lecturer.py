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
        