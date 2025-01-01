import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class EmailSender:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def send_email(self, recipient_email, subject, message):
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(self.email, self.password)

            email_message = MIMEMultipart()
            email_message["From"] = self.email
            email_message["To"] = recipient_email
            email_message["Subject"] = subject
            email_message.attach(MIMEText(message, "plain"))

            server.sendmail(self.email, recipient_email, email_message.as_string())
            server.quit()
        except Exception as e:
            raise Exception(f"Error sending email: {e}")
