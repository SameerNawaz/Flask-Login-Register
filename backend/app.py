from flask import Flask
import sqlalchemy
from flask_login import LoginManager

from models import db, Users

from index import index
from login import login
from logout import logout
from register import register
from home import home
import os

app = Flask(__name__, static_folder='../frontend/static')

app.config['SECRET_KEY'] = 'secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../database.db'

login_manager = LoginManager()
login_manager.init_app(app)
db.init_app(app)
app.app_context().push()

app.register_blueprint(index)
app.register_blueprint(login)
app.register_blueprint(logout)
app.register_blueprint(register)
app.register_blueprint(home)

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

if __name__ == '__main__':
    port = int(os.environ.get('PORT',3000))
    app.run(debug=True, host='0.0.0.0', port=port)
