def create_module(app, **kwargs):
    from .controllers import projects
    app.register_blueprint(projects)
