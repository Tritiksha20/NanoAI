import pytest
from app import create_app, db

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.app_context():
        db.create_all()
        yield app

def test_home(app):
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b'Where care feels like home' in response.data

def test_services(app):
    client = app.test_client()
    response = client.get('/services')
    assert response.status_code == 200

def test_contact_post(app):
    client = app.test_client()
    response = client.post('/contact', data={'name': 'Test', 'email': 'test@example.com', 'message': 'Hi'})
    assert response.status_code == 302  # Redirect