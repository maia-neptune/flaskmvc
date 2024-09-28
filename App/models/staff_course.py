from App.database import db


class StaffCourse(db.Model):
    __tablename__ = 'staff_course'
    id = db.Column(db.Integer, primary_key = True)
    courseID = db.Column(db.Integer, db.ForeignKey('course.id'), nullable = False, unique = True)
    lecturerID = db.Column(db.Integer, db.ForeignKey('lecturer.id'), nullable = True)
    teachingAssistantID = db.Column(db.Integer, db.ForeignKey('teaching_assistant.id'), nullable= True)
    tutorID = db.Column(db.Integer, db.ForeignKey('tutor.id'), nullable= True)

    def __init__(self, courseID, lecturerID, teachingAssistantID, tutorID):
        self.courseID = courseID
        self.lecturerID = lecturerID
        self.teachingAssistantID = teachingAssistantID
        self.tutorID = tutorID 

    def get_json(self):
        return{
            'id': self.id,
            'courseID': self.courseID,
            'lecturerID': self.lecturerID,
            'teachingAssistantID': self.teachingAssistantID,
            'tutorID': self.tutorID
        }