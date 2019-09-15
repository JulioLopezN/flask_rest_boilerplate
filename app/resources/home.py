from datetime import datetime
from flask import Blueprint

home_api = Blueprint('home', __name__)


@home_api.route('/', methods=['GET'])
def home():
    return {'message': datetime.utcnow().isoformat()}
