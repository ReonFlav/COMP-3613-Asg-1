from App.database import db


class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'), nullable=False)
    applicant_id = db.Column(db.Integer, db.ForeignKey('applicant.id'), nullable=False)
    status = db.Column(db.String(50), default='Applied', nullable=False)

    def __init__(id, job_id, applicant_id):
        new_application = Application(id=id, job_id=job_id, applicant_id=applicant_id)
        return new_application
    
    def get_json(self):
        return{
            'id': self.id,
            'job_id': self.job_id,
            'applicant_id': self.applicant_id,
            'status': self.status
        }