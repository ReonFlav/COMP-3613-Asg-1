from .user import *
from .auth import *
from .initialize import *
from .job import *
from .applicant import *
from .application import *

"""def create_job(title, description, company):
    new_job = Job(title=title, description=description, company=company)
    db.session.add(new_job)
    db.session.commit()

def create_applicant(id, name, resume):
    new_applicant= Applicant(id=id, name=name, resume=resume)
    db.session.add(new_applicant)
    db.session.commit()

def create_application(id, job_id, applicant_id, status):
    new_applicant= Application(id=id, job_id=job_id, applicant_id=applicant_id, status=status)
    db.session.add(new_applicant)
    db.session.commit()"""