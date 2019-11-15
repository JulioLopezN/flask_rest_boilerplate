
import os
from flask import Flask, Blueprint
from flask_migrate import Migrate, MigrateCommand
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_marshmallow import Marshmallow

from app.config import configuration
from app.common.security.jwt_manager import JwtManager

app = Flask(__name__)
db = SQLAlchemy()
bcrypt = Bcrypt()
migrate = Migrate(app, db)
ma = Marshmallow(app)
config = configuration[os.getenv('FLASK_ENV') or 'development']

app.config.from_object(config)
db.init_app(app)
bcrypt.init_app(app)

app.app_context().push()

if __name__ == '__main__':
    app.run(debug=False)

jwt_manager = JwtManager(config.SECRET_KEY)

from app.resources import todo_api, home_api, auth_api

app.register_blueprint(home_api)
app.register_blueprint(todo_api)
app.register_blueprint(auth_api)
