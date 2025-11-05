from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user, login_user, logout_user
from app import db
from app.models import Service, BookingRequest, ContactMessage, AdminUser
from app.forms import BookingForm, ContactForm
import os

main_bp = Blueprint('main', __name__)
admin_bp = Blueprint('admin', __name__)

@main_bp.route('/')
def index():
    services = Service.query.limit(6).all()  # Primary services
    return render_template('index.html', services=services)

@main_bp.route('/about')
def about():
    return render_template('about.html')

@main_bp.route('/services')
def services():
    services = Service.query.all()
    return render_template('services.html', services=services)

@main_bp.route('/services/<int:service_id>')
def service_detail(service_id):
    service = Service.query.get_or_404(service_id)
    form = BookingForm()
    return render_template('service_detail.html', service=service, form=form)

@main_bp.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        msg = ContactMessage(name=form.name.data, email=form.email.data, message=form.message.data)
        db.session.add(msg)
        db.session.commit()
        flash('Message sent successfully!')
        # TODO: Send email notification (configure SMTP)
        return redirect(url_for('main.contact'))
    return render_template('contact.html', form=form)

@main_bp.route('/book-service', methods=['GET', 'POST'])
def book_service():
    form = BookingForm()
    if form.validate_on_submit():
        booking = BookingRequest(
            patient_name=form.patient_name.data,
            phone=form.phone.data,
            email=form.email.data,
            address=form.address.data,
            service_id=form.service.data,
            preferred_date=form.preferred_date.data,
            notes=form.notes.data
        )
        db.session.add(booking)
        db.session.commit()
        flash('Booking request submitted!')
        # TODO: Send email notification
        return redirect(url_for('main.index'))
    return render_template('book_service.html', form=form)

@main_bp.route('/privacy')
def privacy():
    return render_template('privacy.html')

@main_bp.route('/terms')
def terms():
    return render_template('terms.html')

@admin_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = AdminUser.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('admin.dashboard'))
        flash('Invalid credentials')
    return render_template('admin_login.html')  # Add this template

@admin_bp.route('/dashboard')
@login_required
def dashboard():
    bookings = BookingRequest.query.all()
    messages = ContactMessage.query.all()
    return render_template('admin_dashboard.html', bookings=bookings, messages=messages)

@admin_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))