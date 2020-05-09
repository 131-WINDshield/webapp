release: flask db upgrade
web: gunicorn wsgi:app

db_init: python -c "from main import db; db.create_all()"
db_upgrade: python manage.py db upgrade