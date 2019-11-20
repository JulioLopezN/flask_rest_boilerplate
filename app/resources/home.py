from datetime import datetime
from flask import Blueprint

home_api = Blueprint('home', __name__)


@home_api.route('/', methods=['GET'])
def index():
    return {'message': datetime.utcnow().isoformat()}
