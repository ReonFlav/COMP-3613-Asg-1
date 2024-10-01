from App.database import db

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    company = db.Column(db.String(100), nullable=False)

    def __init__(title, description, company, location):
        new_job = Job(title=title, description=description, company=company, location=location)
        return new_job
    
    def get_json(self):
        return{
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'company': self.company
        }