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

def assign_lecturer_to_course(courseid, lecturer_id):
    course = Course.query.filter_by(id=courseid).first()
    lecturer = Lecturer.query.filter_by(id=lecturer_id).first()
    lecturerCheck = StaffCourse.query.filter_by(courseID=courseid).first()

    if lecturer is not None and lecturerCheck and lecturerCheck.lecturerID == lecturer.id:
        return "Lecturer already assigned to course."

    lecturerOld = Lecturer.query.filter_by(id=lecturerCheck.lecturerID).first() if lecturerCheck else None

    if lecturerOld and lecturer:
        add_lecturer(courseid, lecturer_id)
        return f"{lecturerOld.prefix} {lecturerOld.firstName} {lecturerOld.lastName} replaced by {lecturer.prefix} {lecturer.firstName} {lecturer.lastName}."

    if course:
        if lecturer:
            add_lecturer(courseid, lecturer_id)
            return f"{lecturer.prefix} {lecturer.firstName} {lecturer.lastName} now assigned to {course.name}."
        else:
            return "Lecturer does not exist."
    else:
        return "Course does not exist."
