
import os
from flask import Flask, Blueprint
from flask_migrate import Migrate, MigrateCommand
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_marshmallow import Marshmallow

from app.config import configuration

app = Flask(__name__)
db = SQLAlchemy()
flask_bcrypt = Bcrypt()
migrate = Migrate(app, db)
ma = Marshmallow(app)

app.config.from_object(configuration[os.getenv('FLASK_ENV') or 'development'])
db.init_app(app)
flask_bcrypt.init_app(app)

app.app_context().push()

if __name__ == '__main__':
    app.run(debug=False)


from app.resources import todo_api, home_api

app.register_blueprint(home_api)
app.register_blueprint(todo_api)
