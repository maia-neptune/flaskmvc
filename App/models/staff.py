from App.database import db

class Staff(db.Model):
    __tablename__ = 'staff'
    id = db.Column(db.Integer, primary_key= True)
    prefix = db.Column(db.String(5), nullable = False)
    firstName = db.Column(db.String(80), nullable = False)
    lastName = db.Column(db.String(80), nullable = False)
    faculty = db.Column(db.String(120), nullable = False)


    def __init__(self, prefix, firstName, lastName, faculty):
        self.prefix = prefix
        self.firstName = firstName
        self.lastName = lastName
        self.faculty = faculty


    def get_json(self):
        return{
            'id': self.id,
            'prefix': self.prefix,
            'firstName': self.firstName,
            'lastName': self.lastName,
            'faculty': self.faculty
     }