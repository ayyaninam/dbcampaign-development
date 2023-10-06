import requests
from celery import shared_task
import datetime
from django.core.mail import send_mail
from django.conf import settings

def mail_sender(sender_email, sender_email_password, receiver_emaill, text_to_send_user, email_of_user, name_of_user, service_title, phone_number_of_user, desc_provided_by_user):
    settings.EMAIL_HOST_USER = sender_email
    settings.EMAIL_HOST_PASSWORD = sender_email_password
<<<<<<< HEAD
    if (sender_email and sender_email_password):
        send_mail(
            f"Message for {name_of_user}",
            f"{text_to_send_user}",
            sender_email,
            [email_of_user],
            fail_silently=False,
        )
    if (receiver_emaill and sender_email and sender_email_password):
        send_mail(
            f"New Form Filled for {service_title} Service by {name_of_user}",
            f"Name: {name_of_user} \n\nEmail Address: {email_of_user} \n\nPhone Number: {phone_number_of_user} \n\nDescription Provided by User: {desc_provided_by_user}",
            sender_email,
            [receiver_emaill],
            fail_silently=False,
        )
=======
    send_mail(
        f"Message for {name_of_user}",
        f"{text_to_send_user}",
        sender_email,
        [email_of_user],
        fail_silently=False,
    )
    send_mail(
        f"New Form Filled for {service_title} Service by {name_of_user}",
        f"Name: {name_of_user} \n\nEmail Address: {email_of_user} \n\nPhone Number: {phone_number_of_user} \n\nDescription Provided by User: {desc_provided_by_user}",
        sender_email,
        [receiver_emaill],
        fail_silently=False,
    )
>>>>>>> b372cbee3ebc850d66aeeecb2c6b25ea7a7f2d4d


@shared_task
def mail_sender_receiver(sender_email, sender_email_password, receiver_emaill, text_to_send_user, email_of_user, name_of_user, service_title, phone_number_of_user, desc_provided_by_user):
    mail_sender(sender_email, sender_email_password, receiver_emaill, text_to_send_user, email_of_user, name_of_user, service_title, phone_number_of_user, desc_provided_by_user)
