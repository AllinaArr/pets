"""
Can start the app with this command: 
flask --debug --app src/app.py run --port 5555

Can also set environment variables:
export FLASK_APP=src/app.py
export FLASK_DEBUG=1
export FLASK_RUN_PORT=5555
flask run
"""

from flask import Flask
from flask_migrate import Migrate
from models import db


# initialize flask app
app = Flask(__name__)
# tell sqlalchemy how to connect to our db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# add sqlalchemy plugin
db.init_app(app)
# add the alembic plugin
migrate = Migrate(app, db)


@app.route('/')
def get_root():
    return "<h1>Hello</h1>", 200

@app.route('/test')
def test():
    return {'test': "test is json"}, 200

@app.route('/testpost', methods=['POST'])
def test_post():
    return {'test post': 'this is a test'}, 200

@app.route('/param/<int:num>')
def test_param(num):
    return {'your param was': num}