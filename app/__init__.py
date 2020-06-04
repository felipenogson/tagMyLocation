# Este es el template de Flask-user
# voy a partir de aqui y despues crear el mapa, pero primero quiero que nadie pueda
# acceder a el si no se logea.

import datetime
from flask import Flask, request, render_template_string
from flask_babelex import Babel
from flask_sqlalchemy import SQLAlchemy
from flask_user import UserManager, UserMixin
from flask_migrate import Migrate
from config import ConfigClass





    
# Create Flask app load app.config
app = Flask(__name__)
app.config.from_object(__name__+'.ConfigClass')

# Initialize Flask-BabelEx
babel = Babel(app)

# Initialize Flask-SQLAlchemy
db = SQLAlchemy(app)

# Initialize Flask-Migrate
migrate = Migrate(app, db)

from app import routes, models

# Start development web server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)