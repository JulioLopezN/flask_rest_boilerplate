import os
from flask import Flask, Blueprint
from flask_migrate import Migrate, MigrateCommand
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_marshmallow import Marshmallow

from app.config import configuration
from app.common.security.jwt_manager import JwtManager
from app.common.services.smtp_email_service import SmtpEmailService

app = Flask(__name__)
db = SQLAlchemy()
bcrypt = Bcrypt()
migrate = Migrate(app, db)
ma = Marshmallow(app)

app.config.from_object(configuration[os.getenv('FLASK_ENV') or 'development'])
db.init_app(app)
bcrypt.init_app(app)

app.app_context().push()

if __name__ == '__main__':
    app.run()

# configure app services
jwt_manager = JwtManager(app.config['SECRET_KEY'])
email_sender = SmtpEmailService(
    # hostname=app.config['EMAIL_HOST'], 
    # port=app.config['EMAIL_PORT'],
    # ssl=app.config['EMAIL_SSL'],
    # from_address=app.config['EMAIL_FROM_ADDRESS'],
    # username=app.config['EMAIL_USER'],
    # password=app.config['EMAIL_PASS']
)

# import blueprints
from app.resources import todo_api, home_api, auth_api

app.register_blueprint(home_api)
app.register_blueprint(todo_api)
app.register_blueprint(auth_api)
