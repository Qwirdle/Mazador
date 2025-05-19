from flask import Flask, render_template, redirect, request
from flask_login import *
from src.models import db, User
from src.config import *
from datetime import *

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'super-secret-key-change-this'

db.init_app(app)

with app.app_context():
    db.create_all()

    user1 = User(
        username='test',
        password='test',
        role='student',
        created_at=datetime.utcnow()
    )

    db.session.add(user1)
    db.session.commit()

# Will fix when inconvenience is encountered <3
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

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

if __name__ == '__main__':
    app.run(debug=True)