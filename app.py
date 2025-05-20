from flask import Flask, render_template, redirect, request, url_for
from flask_login import *
from src.models import db, User
from src.config import *
from datetime import *
from src.seeding import Seeder
from colorama import init, Fore, Style # For custom console output formatting

init(autoreset=True)

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'super-secret-key-change-this'

db.init_app(app)
seed = Seeder()

with app.app_context():
    db.create_all()

# Seeder function
def seedUsers(count=100, onlyOnEmpty=True):
    with app.app_context():
        if onlyOnEmpty:
            if not db.session.query(User.id).first():
                for i in range(count):
                    db.session.add(seed.getStudent())

                db.session.commit()
                print(Fore.BLUE + f" * Seeded {count} users")
        else:
            for i in range(count):
                db.session.add(seed.getStudent())
            
            db.session.commit()
            print(Fore.BLUE + f" * Seeded {count} users")

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
    return render_template('home.html', SCHOOL_NAME = SCHOOL_NAME, USERNAME = user.username)

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
    seedUsers()
    app.run(debug=True)