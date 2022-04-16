import os
from app import create_app


env = os.environ.get('APP_ENV', 'dev')
app = create_app('config.%Config' % env.capitalize())

if __name__ == '__main__':
    app.run()