from App.models import Application, Job, Applicant
from App.database import db
from .application import *

def create_application(id, job_id, applicant_id, status ):
    new_application = Application(id=id, job_id=job_id, applicant_id=applicant_id, status ="Applied")
    db.session.add(new_application)
    db.session.commit()

def view_applicants(job_id):
    return Application.query.filter_by(job_id=job_id).all()