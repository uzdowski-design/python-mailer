from gmail_adapter import GmailAdapter
from messages import WelcomeMessage
from dotenv import load_dotenv
from os import getenv
from dotenv import load_dotenv, dotenv_values
from os import environ

# Clear existing environment variables
for key in list(environ.keys()):
    if key in dotenv_values():
        del environ[key]

load_dotenv()

mailer = GmailAdapter(
    host="smtp.gmail.com",
    port=465,
    username=getenv("USERNAME"),
    password=getenv("PASSWORD"),
)


mailer.login()
welcome = WelcomeMessage()
mailer.send_mail(
    recipient_email="randexcrap@gmail.com",
    subject="Hello World",
    body=welcome.render(name="Mike"),
)
