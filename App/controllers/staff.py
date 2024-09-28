from App.database import db
from App.models import Staff


def get_all_staff(): 
    
    staff = Staff.query.all()

    if staff:
        return staff
    
    return None


def get_staff_by_faculty(faculty):

    staff = Staff.query.filter_by(faculty = faculty).first()

    if staff:
        return staff
    
    return None


