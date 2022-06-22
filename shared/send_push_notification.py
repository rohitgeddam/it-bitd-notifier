# Create your tasks here
from django.conf import settings
from django.contrib.auth import get_user_model
from users.models import PushNotificationToken
import requests as r

from celery import shared_task


from exponent_server_sdk import (
    DeviceNotRegisteredError,
    PushClient,
    PushMessage,
    PushServerError,
    PushTicketError,
)
from requests.exceptions import ConnectionError, HTTPError

@shared_task
def bulk_send_push_messages(message):
    
    all_tokens = PushNotificationToken.objects.all()
    
    for token in all_tokens:
        send_push_message(token.token, message)

    print("Sent Push Notification")

# Basic arguments. You should extend this function with the push features you
# want to use, or simply pass in a `PushMessage` object.
def send_push_message(token, message, extra=None):
    
    message = {
    'to' : token,
    'title' : message["title"],
    'body' : message["body"]
    }
    
    return r.post('https://exp.host/--/api/v2/push/send', json = message)