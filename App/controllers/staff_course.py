from App.models import StaffCourse, Lecturer, Tutor, TeachingAssistant
from App.database import db

def add_staff(courseID, lecturerID, teachingAssistantID, tutorID):
    staffCourse = StaffCourse(courseID = courseID, lecturerID = lecturerID, teachingAssistantID = teachingAssistantID, tutorID= tutorID)
    db.session.add(staffCourse)
    db.session.commit()
    return staffCourse

def show_staff_in_course(courseID):

    staff_in_course = StaffCourse.query.filter_by(courseID = courseID)

    if staff_in_course:
        return staff_in_course
    
    return None


def add_lecturer(courseID, id):

    lecturer = Lecturer.query.filter_by(id = id).first()

    if lecturer:
        staffCourse = StaffCourse.query.filter_by(courseID = courseID).first()

        if staffCourse:
            staffCourse.lecturerID = id
        return None
    return None

def add_teachingAssistant(courseID, id):

    teachingAssistant = TeachingAssistant.query.filter_by(id = id).first()

    if teachingAssistant:
        staffCourse = StaffCourse.query.filter_by(courseID = courseID).first()

        if staffCourse:
            staffCourse.teachingAssistantID = id
        return None
    return None

def add_tutor(courseID, id):

    tutor = Tutor.query.filter_by(id = id).first()

    if tutor:
        staffCourse = StaffCourse.query.filter_by(courseID = courseID).first()

        if staffCourse:
            staffCourse.tutorID = id
        return None
    return None

