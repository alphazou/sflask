from app import app
from flask import current_app, request, url_for
from jinja2 import Template


print(app.url_map)
print(app.config.get('PORT'))

with app.test_request_context():
    print(url_for('index'))
    print(url_for('item', id=2))