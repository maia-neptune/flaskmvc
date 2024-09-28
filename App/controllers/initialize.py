from .user import create_user
from .lecturer import *
from .tutor import *
from .teaching_assistant import *
from .staff_course import *
from .course import *
from App.database import db


def initialize():
    db.drop_all()
    db.create_all()
    create_course('Introduction to Psychology', 'FSS')
    create_course('Introduction to C++', 'FST')
    create_course('Psychology I', 'FSS')
    create_course('Industrial Statistics', 'FOE')
    create_course('Pharmacology II','FMS')
    create_lecturer('Dr.', 'Mark', 'Long', 'FMS')
    create_lecturer('Mrs.','Hannah', 'Skeete', 'FSS')
    create_lecturer('Mr.','Gordon','Wallace','FST')
    create_lecturer('Dr','Hailey','Singh','FOE')
    create_lecturer('Dr.','Bailey','Wells','FSS')
    create_teaching_assistant('Mr.','Kim','Skeete','FSS')
    create_teaching_assistant('Ms.','Jane','Good','FSS')
    create_teaching_assistant('Ms.','Morgan','King','FMS')
    create_teaching_assistant('Mr.','Brett','Long','FST')
    create_teaching_assistant('Mrs', 'Vikki','Khan','FOE')
    create_tutor('Mr.','John','Lip', 'FOE')
    create_tutor('Dr.', 'Alice', 'Brown', 'FSS')
    create_tutor('Ms.', 'Rachel', 'Green', 'FMS')
    create_tutor('Mr.', 'Michael', 'Smith', 'FST')
    create_tutor('Mr.', 'David', 'Johnson', 'FSS')
    add_staff(1,2,6,12)
    add_staff(2,3,9,14)
    add_staff(3,5,7,15)
    add_staff(4,4,10,11)
    add_staff(5,1,8,13)
    # add_lecturer(1,2)
    # add_lecturer(2,3)
    # add_lecturer(3,5)
    # add_lecturer(4,4)
    # add_lecturer(5,1)
    # add_teachingAssistant(1,6)
    # add_teachingAssistant(2,9)
    # add_teachingAssistant(3,7)
    # add_teachingAssistant(4,10)
    # add_teachingAssistant(5,8)
    # add_tutor(1,12)
    # add_tutor(2,14)
    # add_tutor(3,15)
    # add_tutor(4,11)
    # add_tutor(5,13)



