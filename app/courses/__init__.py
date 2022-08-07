
def create_module(app, **kwargs):
 
    from .controllers import courses
    app.register_blueprint(courses, url_prefix='/course')
