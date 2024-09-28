from App.database import db

class Course(db.Model):
    __tablename__= 'course'
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(150), nullable = False)
    faculty = db.Column(db.String(120), nullable = False)


    def __init__(self, name, faculty):
        self.name = name 
        self.faculty = faculty

    def get_json(self):
        return{
            'name': self.name,
            'faculty': self.faculty
        }