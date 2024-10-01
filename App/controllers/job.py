from App.models import Job, Application, Applicant
from App.database import db
from .job import *

def create_job(title, description, company):
    new_job = Job(title=title, description=description, company=company)
    db.session.add(new_job)
    db.session.commit()
