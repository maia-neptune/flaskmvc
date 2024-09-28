from App.database import db
from App.models.staff import *
from App.models.lecturer import *
from App.models.tutor import *
from App.models.teaching_assistant import *


def get_all_staff():

    staff = Staff.query.with_polymorphic('*').all()

    if staff:
        return staff
    
    return None


def get_staff_by_faculty(faculty):

    staff = Staff.query.filter_by(faculty = faculty).first()

    if staff:
        return staff
    
    return None


