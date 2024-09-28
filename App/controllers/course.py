from App.database import db
from App.models import Course 

def create_course(name, faculty):
    course = Course(name = name, faculty = faculty)
    db.session.add(course)
    db.session.commit()
    return course

def get_course_by_name(name):
    course = Course.query.filter_by(name = name).first()

    if course:
        return course
    
    return None 

def get_course_by_id(id):
    course = Course.query.filter_by(id = id).first()

    if course:
        return course
    
    return None

def get_all_courses():

    courses = Course.query.all()

    if courses:
        return courses
    
    return None

def delete_course(id):

    course = get_course_by_id(id)

    if course: 
        db.session.delete(course)
        db.session.commit()
        return "Course removed."
    else:
        return None