import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class GmailAdapter:
    def __init__(self, host: str, port: int, username: str, password: str):
        self.username = username
        self.password = password
        self.server = smtplib.SMTP_SSL(host, port)

    def login(self):
        self.server.ehlo()
        self.server.login(self.username, self.password)

    def _create_message(self, recipient_email, subject, body):
        message = MIMEMultipart()
        message["From"] = self.username
        message["To"] = recipient_email
        message["Subject"] = subject
        message.attach(MIMEText(body, "html"))
        return message

    def send_mail(self, recipient_email: str, subject: str, body: str):
        message = self._create_message(recipient_email, subject, body)
        self.server.sendmail(self.username, recipient_email, message.as_string())

    def __del__(self):
        self.server.close()
