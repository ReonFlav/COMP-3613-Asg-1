from App.models import Applicant, Application, Job
from App.database import db
from .applicant import *


def create_applicant(id, name, resume):
    new_application = Application(id=id, name=name, resume=resume)
    db.session.add(new_application)
    db.session.commit()

def apply_to_job(job_id, applicant_name, resume, applicant_id):
    job_applicant = Applicant(job_id=job_id, name=applicant_name, resume=resume)
    db.session.add(job_applicant)
    db.session.commit()

    application = Application(job_id=job_id, applicant_id=applicant_id)
    db.session.add(application)
    db.session.commit()

def view_jobs():
    return Job.query.all()