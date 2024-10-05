import os, tempfile, pytest, logging, unittest
from werkzeug.security import check_password_hash, generate_password_hash

from App.main import create_app
from App.database import db, create_db
from App.models import User, Lecturer, Tutor, TeachingAssistant, Course
from App.controllers import *


LOGGER = logging.getLogger(__name__)

'''
   Unit Tests
'''
class UserUnitTests(unittest.TestCase):

    def test_new_user(self):
        user = User("bob", "bobpass")
        assert user.username == "bob"

    # pure function no side effects or integrations called
    def test_get_json(self):
        user = User("bob", "bobpass")
        user_json = user.get_json()
        self.assertDictEqual(user_json, {"id":None, "username":"bob"})
    
    def test_hashed_password(self):
        password = "mypass"
        hashed = generate_password_hash(password, method='sha256')
        user = User("bob", password)
        assert user.password != password

    def test_check_password(self):
        password = "mypass"
        user = User("bob", password)
        assert user.check_password(password)

'''
    Integration Tests
'''

# This fixture creates an empty database for the test and deletes it after the test
# scope="class" would execute the fixture once and resued for all methods in the class
@pytest.fixture(autouse=True, scope="module")
def empty_db():
    app = create_app({'TESTING': True, 'SQLALCHEMY_DATABASE_URI': 'sqlite:///test.db'})
    create_db()
    yield app.test_client()
    db.drop_all()


def test_authenticate():
    user = create_user("bob", "bobpass")
    assert login("bob", "bobpass") != None

class UsersIntegrationTests(unittest.TestCase):
# ! all user test 
    def test_create_user(self):
        user = create_user("rick", "bobpass")
        assert user.username == "rick"

    def test_get_all_users_json(self):
    
        users_json = get_all_users_json()
        expected_json = [
            {"id": 1, "username": "bob"},
            {"id": 2, "prefix": "Dr.", "firstName": "John", "lastName": "Doe", "faculty": "FOE", "job": "Lecturer"},
            {"id": 3, "username": "rick"}
        ]
        self.assertListEqual(expected_json, users_json)


    # Tests data changes in the database
    def test_update_user(self):
        update_user(1, "ronnie")
        user = get_user(1)
        assert user.username == "ronnie"

     # Integration Tests for Lecturer Creation
    def test_create_and_confirm_lecturer(self):
        prefix = "Dr."
        firstname = "John"
        lastname = "Doe"
        faculty = "FOE"
        username = "johndoe"
        password = "password123"

        result = create_and_confirm_lecturer(prefix, firstname, lastname, faculty, username, password)

        assert "Lecturer created: Dr. John Doe" in result

        lecturer = Lecturer.query.filter_by(username=username).first()
        assert lecturer is not None
        assert lecturer.firstName == firstname
        assert lecturer.lastName == lastname
        assert lecturer.faculty == faculty

        
    def test_create_lecturer_with_invalid_prefix(self):
        prefix = "InvalidPrefix"
        firstname = "Jane"
        lastname = "Doe"
        faculty = "FOE"
        username = "janedoe"
        password = "password123"

        result = create_and_confirm_lecturer(prefix, firstname, lastname, faculty, username, password)

        assert result == "Invalid prefix. Use: Prof., Dr., Mrs., Mr., or Ms."

    def test_create_lecturer_with_invalid_faculty(self):
        prefix = "Dr."
        firstname = "Jane"
        lastname = "Doe"
        faculty = "InvalidFaculty"
        username = "janedoe"
        password = "password123"


        result = create_and_confirm_lecturer(prefix, firstname, lastname, faculty, username, password)


        assert result == "Invalid faculty. Use: FOE, FST, FSS, FMS, FHE, FOL, FFA, or FOS"


    # Integration Tests for Tutor Creation
    # !
    def test_create_and_confirm_tutor(self):
        prefix = "Mr."
        firstname = "John"
        lastname = "Doe"
        faculty = "FOE"
        username = "johnathondoe"
        password = "password123"

        result = create_and_confirm_tutor(prefix, firstname, lastname, faculty, username, password)

        assert "Tutor created: Mr. John Doe" in result

        tutor = Tutor.query.filter_by(username=username).first()
        assert tutor is not None
        assert tutor.firstName == firstname
        assert tutor.lastName == lastname
        assert tutor.faculty == faculty

# !
    def test_create_tutor_with_invalid_prefix(self):
            prefix = "InvalidPrefix"
            firstname = "Jane"
            lastname = "Doe"
            faculty = "FOE"
            username = "janedoe"
            password = "password123"

            result = create_and_confirm_tutor(prefix, firstname, lastname, faculty, username, password)

            assert result == "Invalid prefix. Use: Prof., Dr., Mrs., Mr., or Ms."

    def test_create_tutor_with_invalid_faculty(self):
        prefix = "Ms."
        firstname = "Jane"
        lastname = "Doe"
        faculty = "InvalidFaculty"
        username = "janedoe"
        password = "password123"


        result = create_and_confirm_tutor(prefix, firstname, lastname, faculty, username, password)


        assert result == "Invalid faculty. Use: FOE, FST, FSS, FMS, FHE, FOL, FFA, or FOS"

        # Integration Tests for Teaching Assisstant Creation
        # !
    def test_create_and_confirm_teaching_assistant(self):
        prefix = "Mr."
        firstname = "John"
        lastname = "Doe"
        faculty = "FOE"
        username = "johnnydoe"
        password = "password123"

        result = create_and_confirm_ta(prefix, firstname, lastname, faculty, username, password)
        print(username)
        assert "Teaching Assistant created: Mr. John Doe" in result

        teaching_assistant = TeachingAssistant.query.filter_by(username=username).first()
        assert teaching_assistant is not None
        assert teaching_assistant.firstName == firstname
        assert teaching_assistant.lastName == lastname
        assert teaching_assistant.faculty == faculty

    def test_create_ta_with_invalid_prefix(self):
            prefix = "InvalidPrefix"
            firstname = "Jane"
            lastname = "Doe"
            faculty = "FOE"
            username = "janedoe"
            password = "password123"

            result = create_and_confirm_ta(prefix, firstname, lastname, faculty, username, password)

            assert result == "Invalid prefix. Use: Dr., Mrs., Mr., or Ms."

    def test_create_ta_with_invalid_faculty(self):
        
        prefix = "Ms."
        firstname = "Jane"
        lastname = "Doe"
        faculty = "InvalidFaculty"
        username = "janedoe"
        password = "password123"

        
        result = create_and_confirm_ta(prefix, firstname, lastname, faculty, username, password)

        
        assert result == "Invalid faculty. Use: FOE, FST, FSS, FMS, FHE, FOL, FFA, or FOS"