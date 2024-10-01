import click, pytest, sys
from flask import Flask
from flask.cli import with_appcontext, AppGroup

from App.database import db, get_migrate
from App.models import User, Job, Application, Applicant
from App.main import create_app
from App.controllers import ( create_user, get_all_users_json, get_all_users, initialize, create_job, view_jobs, apply_to_job, view_applicants )

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jobs.db'
db.init_app(app)



# This commands file allow you to create convenient CLI commands for testing controllers

app = create_app()
migrate = get_migrate(app)

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def init():
    initialize()
    print('database intialized')

'''
User Commands
'''

# Commands can be organized using groups

# create a group, it would be the first argument of the comand
# eg : flask user <command>
user_cli = AppGroup('user', help='User object commands') 

# Then define the command and any parameters and annotate it with the group (@)
@user_cli.command("create", help="Creates a user")
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
def create_user_command(username, password):
    create_user(username, password)
    print(f'{username} created!')

# this command will be : flask user create bob bobpass

@user_cli.command("list", help="Lists users in the database")
@click.argument("format", default="string")
def list_user_command(format):
    if format == 'string':
        print(get_all_users())
    else:
        print(get_all_users_json())

# My custom commands
@app.cli.command("create-job")
def create_job_cli():
    title = input("Job Title: ")
    description = input("Job Description: ")
    company = input("Company: ")
    create_job(title, description, company)
    print("Job created!")

@app.cli.command("view-jobs")
def view_jobs_cli():
    jobs = view_jobs()
    for job in jobs:
        print(f"ID: {job.id}, Title: {job.title}, Company: {job.company}")

@app.cli.command("apply-job")
def apply_job_cli():
    job_id = int(input("Job ID: "))
    name = input("Your Name: ")
    resume = input("Your Resume: ")
    apply_to_job(job_id, name, resume)
    print("Application submitted!")

@app.cli.command("view-applicants")
def view_applicants_cli():
    job_id = int(input("Job ID: "))
    applicants = view_applicants(job_id)
    for applicant in applicants:
        print(f"Applicant ID: {applicant.applicant_id}, Status: {applicant.status}")


app.cli.add_command(user_cli) # add the group to the cli

if __name__ == "__main__":
    app.run()

'''
Test Commands
'''

test = AppGroup('test', help='Testing commands') 

@test.command("user", help="Run User tests")
@click.argument("type", default="all")
def user_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "UserUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "App"]))
    

app.cli.add_command(test)