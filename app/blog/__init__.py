

def create_module(app, **kwargs):
    from .controllers import blog
    app.register_blueprint(blog, url_prefix='/blog')