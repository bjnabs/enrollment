


def create_module(app, **kwargs):
    from .routes import main
    app.register_blueprint(main)