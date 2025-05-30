# The code in this file use of 
# python libaries that are seperate from django libaries

from django.core.mail import send_mail

def auto_mail_reply(recipient):
    subject = "Greetings"
    message = "Hello! Thank you for contacting Granzular Codex. Looking forward to strike wonderful deals with you."
    sender = None # sender email specified in settings would be used
    send_mail(
            subject,
            message,
            sender,
            [recipient],
            fail_silently=False,

        )
