# FastAPI code

from typing import Optional

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from email_notifications.templates import *
from email_notifications.utils import *

app = FastAPI()

# Set up CORS
origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/send_welcome_email")
def send_welcome_email(recipient: str, template_data: dict):
    """Send a welcome email with personalized content to a new user"""
    email_template = WelcomeEmailTemplate(template_data)
    email_message = create_email_message(recipient, email_template)
    send_email(email_message)


@app.post("/send_password_reset_email")
def send_password_reset_email(recipient: str, template_data: dict):
    """Send a password reset email with personalized content to the user"""
    email_template = PasswordResetEmailTemplate(template_data)
    email_message = create_email_message(recipient, email_template)
    send_email(email_message)


@app.post("/send_order_confirmation_email")
def send_order_confirmation_email(recipient: str, template_data: dict):
    """Send an order confirmation email with personalized content to the user"""
    email_template = OrderConfirmationEmailTemplate(template_data)
    email_message = create_email_message(recipient, email_template)
    send_email(email_message)


@app.post("/send_account_activity_alert_email")
def send_account_activity_alert_email(recipient: str, template_data: dict):
    """Send an account activity alert email with personalized content to the user"""
    email_template = AccountActivityAlertEmailTemplate(template_data)
    email_message = create_email_message(recipient, email_template)
    send_email(email_message)


@app.get("/get_email_delivery_status")
def get_email_delivery_status(email_id: str):
    """Get the delivery status of a sent email"""
    return get_delivery_status(email_id)


@app.get("/get_email_logs")
def get_email_logs(email_id: str):
    """Get the logs for a sent email"""
    return get_logs(email_id)