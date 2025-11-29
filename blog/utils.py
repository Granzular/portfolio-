# The code in this file use of 
# python libaries that are seperate from django libaries

from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives

def auto_mail_reply(recipient):
    subject = "Thank You for Contacting Granzular Codex"
    from_email = "no-reply@granzularcodex.com"
    to = [recipient]
    text_content = "Hello! Thank you for contacting Granzular Codex. Looking forward to striking wonderful deals with you."
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <title>Thank You - Granzular Codex</title>
    <style>
    body {
    background-color: #f4f4f7;
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    color: #333;
    }
    .container {
    max-width: 600px;
    margin: 30px auto;
    background-color: #ffffff;
    padding: 30px;
    border-radius: 10px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }
    h1 {
    color: #2b2e83;
    font-size: 24px;
    }
    p {
    font-size: 16px;
    line-height: 1.6;
    }
    .footer {
    margin-top: 30px;
    font-size: 13px;
    color: #888;
    text-align: center;
    }
    .brand {
    font-weight: bold;
    color: #2b2e83;
    }
    </style>
    </head>
    <body>
    <div class="container">
    <h1>Hello!</h1>
    <p>Thank you for contacting <span class="brand">Granzular Codex</span>.</p>
    <p>We're excited about the opportunity to strike wonderful deals with you. Stay tuned!</p>
    <div class="footer">
    &copy; 2025 Granzular Codex. All rights reserved.
    </div>
    </div>
    </body>
    </html>
    """

    msg = EmailMultiAlternatives(subject, text_content, from_email, to)
    msg.attach_alternative(html_content, "text/html")
    msg.send()

def get_tech_logos()-> dict:
    logo_dict = {"python" : "[![Python](https://img.icons8.com/color/96/python.png)](https://www.python.org)",
                 "django" : "[![Django](https://img.icons8.com/color/96/django.png)](https://www.djangoproject.com)",
                 "javascript" : "[![JavaScript](https://img.icons8.com/color/96/javascript.png)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)",
                 "react" : "[![React](https://img.icons8.com/color/96/react-native.png)](https://react.dev)",
                 "nextjs" : "[![Next.js](https://img.icons8.com/color/96/nextjs.png)](https://nextjs.org)",
                 "postgres" : "[![PostgreSQL](https://img.icons8.com/color/96/postgresql.png)](https://www.postgresql.org)",
                 "mysql" : "[![MySQL](https://img.icons8.com/color/96/mysql-logo.png)](https://www.mysql.com)",
                 "redis" : "[![Redis](https://img.icons8.com/color/96/redis.png)](https://redis.io)",
                 "linux" : "[![Linux](https://img.icons8.com/color/96/linux.png)](https://www.kernel.org)",
                 "git" : "[![Git](https://img.icons8.com/color/96/git.png)](https://git-scm.com)",
                             }
    return logo_dict
