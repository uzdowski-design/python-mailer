# Mailer

Python application to send automated emails. Can be use for newsletters, notifications, etc.

Send emails with html email templates.

## Development

Run `python -m venv venv` to create virtualenv.

Run `source venv/bin/activate` to activate virtualenv.

Run `deactivate` to deactivate virtualenv after development is finished.

Run `pip install requirements.txt -r` to install dependencies.

## Usage

Configure object passed to `mailer.send_mail()` method to send emails.

Use/add templates in `/templates` folder to create emails html.

In PASSWORD env variable put **Google's app password** instead Google's account email password.  
Doc: [https://support.google.com/accounts/answer/185833?hl=en](https://support.google.com/accounts/answer/185833?hl=en)
