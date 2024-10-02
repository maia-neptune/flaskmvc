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
    
def assign_ta(courseid, ta_id):
    course = Course.query.filter_by(id=courseid).first()
    ta = TeachingAssistant.query.filter_by(id=ta_id).first()
    taCheck = StaffCourse.query.filter_by(courseID=courseid).first()

    if ta is not None and taCheck and taCheck.teachingAssistantID == ta.id:
        return "Teaching assistant already assigned to course."

    taOld = TeachingAssistant.query.filter_by(id=taCheck.teachingAssistantID).first() if taCheck else None

    if taOld and ta:
        add_teachingAssistant(courseid, ta_id)
        return f"{taOld.prefix} {taOld.firstName} {taOld.lastName} replaced by {ta.prefix} {ta.firstName} {ta.lastName}."

    if course:
        if ta:
            add_teachingAssistant(courseid, ta_id)
            return f"{ta.prefix} {ta.firstName} {ta.lastName} now assigned to {course.name}."
        else:
            return "Teaching assistant does not exist."
    else:
        return "Course does not exist."
