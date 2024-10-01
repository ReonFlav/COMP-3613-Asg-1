from App.database import db

class Applicant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    resume = db.Column(db.Text, nullable=True)

    def __init__(id, name, resume):
        new_applicant = Applicant(id=id, name=name, resume=resume)
        return new_applicant
    
    def get_json(self):
        return{
            'id': self.id,
            'name': self.name,
            'resume': self.resume
        }