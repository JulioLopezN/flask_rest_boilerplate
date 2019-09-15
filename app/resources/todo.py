from flask import Blueprint, request, jsonify
from datetime import datetime
from app import db
from app.models import Todo as Model
from app.schemas import TodoSchema as EntitySchema

todo_api = Blueprint('todo', __name__, url_prefix='/todos')

entity_schema = EntitySchema()
entities_schema = EntitySchema(many=True)


@todo_api.route('/', methods=['GET'])
def getAll():
    data = Model.query.all()

    return jsonify(entities_schema.dump(data))


@todo_api.route('/<int:id>', methods=['GET'])
def get(id):
    entity = Model.query.filter(Model.id == id).first()
    if entity is None:
        return {'error': 'Entity not found'}, 404

    return jsonify(entity_schema.dump(entity))


@todo_api.route('/', methods=['POST'])
def add():
    entity = entity_schema.load(request.json, partial=True)
    db.session.add(entity)
    db.session.commit()

    return entity_schema.dump(entity)


@todo_api.route('/<int:id>', methods=['PUT'])
def update(id):
    entity = Model.query.filter(Model.id == id).first()
    if entity is None:
        return {'error': 'Entity not found'}, 404

    model = entity_schema.load(request.json, partial=True)

    entity.description = model.description
    entity.done = model.done

    db.session.commit()

    return entity_schema.dump(entity)


@todo_api.route('/<int:id>', methods=['DELETE'])
def delete(id):
    entity = Model.query.filter(Model.id == id).first()
    if entity is None:
        return {'error': 'Entity not found'}, 404

    db.session.delete(entity)
    db.session.commit()

    return entity_schema.dump(entity)
