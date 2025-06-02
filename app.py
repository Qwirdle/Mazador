from flask import Flask, render_template, redirect, request, url_for
from flask_login import *
from src.models import db, User, Class
from src.config import *
from src.util import loadMarkdownAsHTML
from datetime import *
from src.seeding import Seeder
from colorama import init, Fore, Style # For custom console output formatting
import os, random

root = os.path.abspath(os.getcwd())

init(autoreset=True)

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'super-secret-key-change-this' # Change this Jasper, for the love of God

db.init_app(app)
seed = Seeder()

with app.app_context():
    db.create_all()

# Seeder functions
def seedStudents(count=100):
    with app.app_context():
        for i in range(count):
            db.session.add(seed.getStudent())
        
        db.session.commit()
        print(Style.BRIGHT + Fore.BLUE + f" * Seeded {count} students")

def seedFaculty(count=10):
    with app.app_context():
        for i in range(count):
            db.session.add(seed.getFaculty())
        
        db.session.commit()
        print(Style.BRIGHT + Fore.BLUE + f" * Seeded {count} faculty")

def seedClasses(count=40):
    with app.app_context():
        for i in range(count):
            db.session.add(seed.getClass())
        
        db.session.commit()
        print(Style.BRIGHT + Fore.BLUE + f" * Seeded {count} classes")

def enrollStudents(classCount=7):
    students = User.query.filter_by(role='student').all()
    classes = Class.query.all()

    for student in students:
        chosenClasses = random.sample(classes, min(classCount, len(classes)))

        for x in chosenClasses:
            if x not in student.enrolled_classes:
                student.enrolled_classes.append(x)

    db.session.commit()
    print(Style.BRIGHT + Fore.BLUE + f" * Enrolled {len(students)} students into {classCount} classes each")

def enrollFaculty(classCount=3):
    faculty = User.query.filter_by(role='faculty').all()
    classes = Class.query.all()

    for person in faculty:
        chosenClasses = random.sample(classes, min(classCount, len(classes)))

        for x in chosenClasses:
            if x not in person.teaching_classes:
                person.teaching_classes.append(x)

    db.session.commit()
    print(Style.BRIGHT + Fore.BLUE + f" * Added {len(faculty)} faculty into {classCount} classes each")




# Will fix when inconvenience is encountered <3
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/logout/')
def logout():
    logout_user()
    return redirect(url_for("login"))

# Import routes
from src.routes.user_authentication import login


@app.route('/home/')
@login_required
def home():
    user = User.query.filter_by(username=current_user.username).first()
    return render_template('home.html', SCHOOL_NAME = SCHOOL_NAME, USERNAME = user.username, FNAME = user.fname, LNAME = user.lname, ANNOUNCEMENTS = loadMarkdownAsHTML(root + "/data/__announcements.md"))

# Todo: Move to and create error.py routes file
@app.errorhandler(404)
def __error_404(e):
    return redirect('/page-not-found') # Redirects to a different page to allow for CSS to still work properly

@app.route('/page-not-found')
def pageNotFound():
    return render_template('error/404.html')

# Redirect to index when accessing part of site without proper unauthorization
@login_manager.unauthorized_handler
def unauthorized_callback():
    return redirect(url_for('login'))

if __name__ == '__main__':
    with app.app_context():
        if not db.session.query(User.id).first(): # Only seed if unseeded
            seedStudents(2000)
            seedFaculty(150)
            seedClasses(225)
            enrollStudents()
            enrollFaculty()

    app.run(debug=True)