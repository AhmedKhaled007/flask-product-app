import os

from product_app import create_app
from product_app.extensions import db
config_name = os.environ.get('FLASK_CONFIG', 'development')
app = create_app(config_name)
db.create_all(app=create_app())

if __name__ == '__main__':
    app.run()
