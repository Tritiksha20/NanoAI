from app import create_app, db
from app.models import Service, AdminUser

app = create_app()

with app.app_context():
    db.create_all()
    
    # Seed admin user
    admin = AdminUser(username='admin')
    admin.set_password('password')  # Change in production
    db.session.add(admin)
    
    # Seed services from PDF (simulated)
    services_data = [
        {"name": "Bedside Caregivers", "description": "Compassionate bedside caregivers provide round-the-clock support for daily activities. Sourced from attached PDF: Services section.", "faqs": "What is included? Basic care.", "pricing": "$50/day"},
        {"name": "Skilled Nursing Care", "description": "Professional nursing for medical needs. Sourced from attached PDF.", "faqs": "Qualifications? RN certified.", "pricing": "$100/day"},
        # Add all 7 services similarly...
    ]
    for data in services_data:
        service = Service(**data)
        db.session.add(service)
    
    db.session.commit()
    print("Database initialized.")