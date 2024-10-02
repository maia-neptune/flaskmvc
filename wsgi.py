import click, pytest, sys
from flask import Flask
from flask.cli import with_appcontext, AppGroup

from App.database import db, get_migrate
from App.models import User, Course, Staff, StaffCourse, Lecturer, TeachingAssistant, Tutor
from App.main import create_app
from App.controllers import *


# This commands file allow you to create convenient CLI commands for testing controllers

app = create_app()
migrate = get_migrate(app)

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def init():
    initialize()
    print('database intialized')

#this command shows list of all staff
@app.cli.command("staff", help="Shows all staff")
def show_staff():
    staff = get_all_staff()

    if staff:
        print('Full Staff List:')
        for member in staff:
            print(member.id, member.prefix, member.firstName, member.lastName, member.faculty, member.job)
    else:
        print('No staff present.')

#this command shows the list of all courses 
@app.cli.command("courses", help="Shows the list of all courses")
def courses_list():
    courses = get_all_courses()

    print('Course list: \n')
    if courses:
        for course in courses:
            print(course.id, course.name, course.faculty)

    else:
        print('No courses available.')

#this command shows a list of all staff in the selected course id
@app.cli.command("courseStaff", help="Shows all staff for the course code entered")
@click.argument("courseid")
def show_course_staff(courseid):
    
    course_staff = show_staff_in_course(courseid)

    if course_staff:
        course = Course.query.filter_by(id = course_staff.courseID).first()
        lecturer = Lecturer.query.filter_by(id = course_staff.lecturerID).first()
        tutor = Tutor.query.filter_by(id = course_staff.tutorID).first()
        teachingAssistant = TeachingAssistant.query.filter_by(id= course_staff.teachingAssistantID).first()

        if course:
            print(course.name, course.faculty, ':\n')

        if lecturer:
            print(lecturer.id, lecturer.prefix, lecturer.firstName, lecturer.lastName, lecturer.faculty, lecturer.job)
        else:
            print('No lecturer available for this course.')
        
        if teachingAssistant:
            print(teachingAssistant.id, teachingAssistant.prefix, teachingAssistant.firstName, teachingAssistant.lastName, teachingAssistant.faculty, teachingAssistant.job)
        else:
            print('No teaching assistant available for this course.')
        
        if tutor:
            print(tutor.id, tutor.prefix, tutor.firstName, tutor.lastName, tutor.faculty, tutor.job)
        else:
            print('No tutor available for this course.')

    else:
        print('Course does not exist.')

#this command creates a course
@app.cli.command("createCourse", help="This command creates a course, Insert the course name in quotes.")
@click.argument("name")
@click.argument("faculty")
def make_course(name, faculty): 

    valid_faculties = ['FOE', 'FST', 'FSS', 'FMS', 'FHE', 'FOL', 'FFA', 'FOS']
    if faculty not in valid_faculties:
        print("Incorrect faculty selected. Please use: FOE, FST, FSS, FMS, FHE, FOL, FFA, or FOS")
        return

    course = create_course(name,faculty)
    courseOnly = add_course_only(course.id) #adds to table StaffCourse with no staff

    if course and courseOnly:
        print("Course", course.name, "created. Faculty:", course.faculty, "ID: ", course.id)

    else:
        print('Course not created')

# this command creates a lecturer
@app.cli.command("createLecturer", help="Creates a lecturer. Parameters required: prefix, first name, last name, faculty")
@click.argument("prefix")
@click.argument("firstname")
@click.argument("lastname")
@click.argument("faculty")
def creates_lecturer(prefix, firstname, lastname, faculty):

    valid_prefixes = ['Mrs.', 'Dr.', 'Mr.', 'Ms.', 'Prof.']
    if prefix not in valid_prefixes:
        print("Incorrect prefix. Please use: Prof., Dr., Mrs., Mr., or Ms.")
        return
    
    valid_faculties = ['FOE', 'FST', 'FSS', 'FMS', 'FHE', 'FOL', 'FFA', 'FOS']
    if faculty not in valid_faculties:
        print("Incorrect faculty selected. Please use: FOE, FST, FSS, FMS, FHE, FOL, FFA, or FOS")
        return

    lecturer = create_lecturer(prefix, firstname, lastname, faculty)

    if lecturer.prefix and lecturer.faculty:
        print('Lecturer created. \n','Hello, ', lecturer.prefix, lecturer.firstName, lecturer.lastName, 'The ', lecturer.faculty, ' is glad to have you.')
        print("Your ID is: ", lecturer.id)
    else:
        print(lecturer)

#this command creates a teaching assistant
@app.cli.command("createTA", help="Creates a teaching assistant. Parameters required: prefix, first name, last name, faculty")
@click.argument("prefix")
@click.argument("firstname")
@click.argument("lastname")
@click.argument("faculty")
def creates_ta(prefix, firstname, lastname, faculty):
 
    valid_prefixes = ['Mrs.', 'Dr.', 'Mr.', 'Ms.', 'Prof.']
    if prefix not in valid_prefixes:
        print("Incorrect prefix. Please use: Prof., Dr., Mrs., Mr., or Ms.")
        return
    
    valid_faculties = ['FOE', 'FST', 'FSS', 'FMS', 'FHE', 'FOL', 'FFA', 'FOS']
    if faculty not in valid_faculties:
        print("Incorrect faculty selected. Please use: FOE, FST, FSS, FMS, FHE, FOL, FFA, or FOS")
        return

    ta = create_teaching_assistant(prefix, firstname, lastname, faculty)

    if ta:
        print('Teaching assistant created. \n','Hello, ', ta.prefix, ta.firstName, ta.lastName, 'The ', ta.faculty, ' is glad to have you.')
        print("Your ID is: ", ta.id)
    else:
        print(ta)   

#this command creates a tutor
@app.cli.command("createTutor", help="Creates a tutor. Parameters required: prefix, first name, last name, faculty")
@click.argument("prefix")
@click.argument("firstname")
@click.argument("lastname")
@click.argument("faculty")
def creates_tutor(prefix, firstname, lastname, faculty):

    valid_prefixes = ['Mrs.', 'Dr.', 'Mr.', 'Ms.', 'Prof.']
    if prefix not in valid_prefixes:
        print("Incorrect prefix. Please use: Prof., Dr., Mrs., Mr., or Ms.")
        return
    
    valid_faculties = ['FOE', 'FST', 'FSS', 'FMS', 'FHE', 'FOL', 'FFA', 'FOS']
    if faculty not in valid_faculties:
        print("Incorrect faculty selected. Please use: FOE, FST, FSS, FMS, FHE, FOL, FFA, or FOS")
        return

    tutor = create_tutor(prefix, firstname, lastname, faculty)

    if tutor.prefix and tutor.faculty:
        print('Tutor created. \n','Hello, ', tutor.prefix, tutor.firstName, tutor.lastName, '. The ', tutor.faculty, ' is glad to have you.')
    else:
        print(tutor) 

#this command removes a lecturer from a course
@app.cli.command("removeLecturer", help="This command removes a lecturer from a course. Requires course id and lecturer id")
@click.argument("courseid")
@click.argument("id")
def remove_lecturer_course(courseid, id):

    response = remove_lecturer_from_course(courseid, id)

    if response != "Lecturer not assigned to selected course.":
        print(response)
    else:
        print("This lecturer doesn't exist or does not teach this course. Use the command flask courseStaff + courseID to see the full list of staff.")

#this command removes a teaching assistant from a course
@app.cli.command("removeTA", help="This command removes a teaching assistant from a course. Requires course id and teaching assistant id")
@click.argument("courseid")
@click.argument("id")
def remove_ta_course(courseid, id):

    response = remove_teachingAssistant_from_course(courseid, id)

    if response:
        print(response)
    else:
        print("This TA doesn't exist or does not teach this course. Use the command flask courseStaff + courseID to see the full list of staff.")

#this command removes a tutor from a course
@app.cli.command("removeTutor", help="This command removes a tutor from a course. Requires course id and tutor id")
@click.argument("courseid")
@click.argument("id")
def remove_tutor_course(courseid, id):

    response = remove_tutor_from_course(courseid, id)

    if response:
        print(response)
    else:
        print("This tutor doesn't exist or does not teach this course. Use the command flask courseStaff + courseID to see the full list of staff.")

#this command removes a course
@app.cli.command("removeCourse", help="Removes a course.")
@click.argument("courseid")
def delete_course_one(courseid):

    response = remove_course_record(courseid)

    if response:
        delete_course(courseid)
        print(response)
    else:
        response = delete_course(courseid)
        if response:
            print(response)
        else:
            print("Course does not exist. Type flask courses to get a full list of courses.")


# this command assigns a lecturer to a course
@app.cli.command("assignLecturer", help="Assigns a lecturer to a course even if a lecturer was already assigned.")
@click.argument("courseid")
@click.argument("id")
def assign_lecturer_command(courseid, id):
    result = assign_lecturer(courseid, id)
    print(result)   

# this command assigns a TA to a course
@app.cli.command("assignTA", help="Assigns a teaching assistant to a course even if a teaching assistant was already assigned.")
@click.argument("courseid")
@click.argument("id")
def assign_ta(courseid, id):

    course = Course.query.filter_by(id = courseid).first()
    ta = TeachingAssistant.query.filter_by(id = id).first()
    taCheck = StaffCourse.query.filter_by(courseID=courseid).first()
    taOld = TeachingAssistant.query.filter_by(id = taCheck.teachingAssistantID).first()

    if ta is not None and taCheck.teachingAssistantID == ta.id:
        print("Teaching assistant already assigned to course.")
        return

    if taOld is not None and ta:
        add_teachingAssistant(courseid, id)
        print(taOld.prefix, taOld.firstName, taOld.lastName, 'replaced by', ta.prefix, ta.firstName, ta.lastName)
    if course:
        if ta:
            add_teachingAssistant(courseid, id)
            print(ta.prefix, ta.firstName, ta.lastName,'now assigned to', course.name, '.')
        else:
            print('Teaching assistant does not exist.')
    else:
        print('Course does not exist.')

# this command assigns a tutor to a course
@app.cli.command("assignTutor", help="Assigns a tutor to a course even if a tutor was already assigned.")
@click.argument("courseid")
@click.argument("id")
def assign_tutor(courseid, id):

    course = Course.query.filter_by(id = courseid).first()
    tutor = Tutor.query.filter_by(id = id).first()
    tutorCheck = StaffCourse.query.filter_by(courseID=courseid).first()
    tutorOld = Tutor.query.filter_by(id = tutorCheck.tutorID).first()

    if tutor is not None and tutorCheck.tutorID == tutor.id:
        print("Tutor already assigned to course.")
        return

    if tutorOld is not None and tutor:
        add_tutor(courseid, id)
        print(tutorOld.prefix, tutorOld.firstName, tutorOld.lastName, 'replaced by', tutor.prefix, tutor.firstName, tutor.lastName)
    if course:
        if tutor:
            add_tutor(courseid, id)
            print(tutor.prefix, tutor.firstName, tutor.lastName,'now assigned to', course.name, '.')
        else:
            print('Tutor does not exist.')
    else:
        print('Course does not exist.')

#fires lecturer
@app.cli.command("fireLecturer", help='Removes lecturer from the database and any course that they would be teaching.')
@click.argument('id')
def remove_lecturer(id):

    lecturer = Lecturer.query.filter_by(id = id).first()

    if lecturer:
        print(lecturer.prefix,lecturer.firstName, lecturer.lastName, end=' ')
        fire_lecturer(id)
        print('has been removed.')
    else:
        print('Lecturer does not exist.')

#fires TA
@app.cli.command("fireTA", help='Removes teaching assistant from the database and any course that they would be teaching.')
@click.argument('id')
def remove_ta(id):

    ta = TeachingAssistant.query.filter_by(id = id).first()

    if ta:
        print(ta.prefix, ta.firstName, ta.lastName, end=' ')
        fire_teaching_assistant(id)
        print('has been removed.')
    else:
        print('Teaching assistant does not exist.')

#fires tutor
@app.cli.command("fireTutor", help='Removes tutor from the database and any course that they would be teaching.')
@click.argument('id')
def remove_tutor(id):

    tutor = Tutor.query.filter_by(id = id).first()

    if tutor:
        print(tutor.prefix, tutor.firstName, tutor.lastName, end=' ')
        fire_tutor(id)
        print('has been removed.')
    else:
        print('Tutor does not exist.')

# '''
# User Commands #irrelevant for Staff Allocations
# '''

# Commands can be organized using groups

# create a group, it would be the first argument of the comand
# eg : flask user <command>
# user_cli = AppGroup('user', help='User object commands') 

# # Then define the command and any parameters and annotate it with the group (@)
# @user_cli.command("create", help="Creates a user")
# @click.argument("username", default="rob")
# @click.argument("password", default="robpass")
# def create_user_command(username, password):
#     create_user(username, password)
#     print(f'{username} created!')

# this command will be : flask user create bob bobpass

# @user_cli.command("list", help="Lists users in the database")
# @click.argument("format", default="string")
# def list_user_command(format):
#     if format == 'string':
#         print(get_all_users())
#     else:
#         print(get_all_users_json())

# app.cli.add_command(user_cli) # add the group to the cli

# '''
# Test Commands
# '''

# test = AppGroup('test', help='Testing commands') 

# @test.command("user", help="Run User tests")
# @click.argument("type", default="all")
# def user_tests_command(type):
#     if type == "unit":
#         sys.exit(pytest.main(["-k", "UserUnitTests"]))
#     elif type == "int":
#         sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
#     else:
#         sys.exit(pytest.main(["-k", "App"]))
    

# app.cli.add_command(test)