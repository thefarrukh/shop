from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
import secrets
import string


def send_email_confirmation(email, token):
    subject = "Confirm your email address"
    to_email = email
    context = {
        "token": token,
        "frontend_url": "eCommerce.com",
    }
    html_content = render_to_string("confirm_email.html", context)
    email = EmailMessage(subject, html_content, to=[to_email])
    email.content_subtype = "html"
    email.send()

def generate_temp_password(length=10):
    characters = string.ascii_letters + string.digits
    return ''.join(secrets.choice(characters) for _ in range(length))


def send_email_confirmation_with_password(email, token):
    temp_password = generate_temp_password()
    subject = "Confirm your email address and temporary password"
    to_email = email
    context = {
        "token": token,
        "frontend_url": "eCommerce.com",
        "password": temp_password,
    }
    html_content = render_to_string("confirm_email_with_password.html", context)
    email = EmailMessage(subject, html_content, to=[to_email])
    email.content_subtype = "html"
    email.send()
    return temp_password  