from flask import Blueprint, render_template, redirect, url_for
from models.models import ParticipantsDB, FightsDB, CompetitionsDB, BacklogDB, RegistrationsDB
from extensions import extensions

db = extensions.db
home = Blueprint('home', __name__, template_folder='templates')

@home.route('/')
def home_view():
    return redirect(url_for('home.competition_start'))

@home.route('/competition_start/')
def competition_start():
    return render_template('competition_start.html')


@home.route('/competition_create_new/')
def competition_create_new():
    try:
        db.session.query(BacklogDB).delete()
        db.session.commit()
    except Exception as e:
        print(e)
    return "hello"
