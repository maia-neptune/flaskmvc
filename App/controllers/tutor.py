from App.database import db
from App.models import Tutor, Course, StaffCourse

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

def add_tutor(courseid, tutorid):
    # Check if the relationship already exists
    existing_assignment = StaffCourse.query.filter_by(courseID=courseid, tutorID=tutorid).first()
    
    if existing_assignment:
        print(f"Tutor ID {tutorid} is already assigned to Course ID {courseid}.")
        return False

    # Create a new StaffCourse entry
    new_assignment = StaffCourse(courseID=courseid, tutorID=tutorid)
    
    # Add to the session and commit to the database
    db.session.add(new_assignment)
    db.session.commit()
    
    print(f"Tutor ID {tutorid} successfully assigned to Course ID {courseid}.")
    return True
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

    
    print(f"Tutor ID {tutorid} successfully assigned to Course ID {courseid}.")
    return True
    
def assign_tutor(courseid, id):
    course = Course.query.filter_by(id=courseid).first()
    tutor = Tutor.query.filter_by(id=id).first()
    tutorCheck = StaffCourse.query.filter_by(courseID=courseid).first()
    tutorOld = Tutor.query.filter_by(id=tutorCheck.tutorID).first()

    if tutor is not None and tutorCheck.tutorID == tutor.id:
        return "Tutor already assigned to course."

    if tutorOld is not None and tutor:
        add_tutor(courseid, id)
        return f"{tutorOld.prefix} {tutorOld.firstName} {tutorOld.lastName} replaced by {tutor.prefix} {tutor.firstName} {tutor.lastName}"

    if course:
        if tutor:
            add_tutor(courseid, id)
            return f"{tutor.prefix} {tutor.firstName} {tutor.lastName} now assigned to {course.name}."
        else:
            return "Tutor does not exist."
    else:
        return "Course does not exist."
