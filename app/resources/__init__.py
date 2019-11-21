def register_resources(app):
    from app.resources.home import home_api
    from app.resources.todo import todo_api
    from app.resources.auth import auth_api

    app.register_blueprint(home_api)
    app.register_blueprint(todo_api)
    app.register_blueprint(auth_api)
