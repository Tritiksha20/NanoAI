# Chessi Healthcare Web App

## Setup
1. Clone or copy files.
2. `python -m venv venv && source venv/bin/activate && pip install -r requirements.txt`
3. `python scripts/init_db.py`
4. `flask run` or `docker-compose up --build`

## Tests
`pytest`

## Deploy
Use gunicorn: `gunicorn app:create_app()`
For HTTPS: Use Let's Encrypt and nginx reverse proxy.