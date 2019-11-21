import os
from flask import Flask, Blueprint, jsonify, request, g
from flask_migrate import Migrate, MigrateCommand
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_marshmallow import Marshmallow

from app.config import configuration
from app.common.security.jwt_manager import JwtManager
from app.common.services.smtp_email_service import SmtpEmailService
from app.resources import register_resources

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

# handler errors
@app.errorhandler(404)
def not_found_error(error):
    return jsonify({
        "code": error.code,
        "name": error.name,
        "description": error.description,
    }), 404

@app.errorhandler(500)
def internal_server_error(err):
    app.logger.error('%s %s: %s', err.code, err.name, err.description)
    return jsonify({
        "code": err.code,
        "name": err.name,
        "description": err.description,
    }), 500

# middlewares
@app.before_request
def load_user():
    authorization_header: str = request.headers.get('Authorization')
    if not authorization_header: return

    token = authorization_header.replace('Bearer ', '')
    if not token: return

    user = jwt_manager.decode(token)
    g.user = user


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

# register blueprints
register_resources(app)
