import logging
from tools.email_sender import EmailSender
from tools.file_loader import FileLoader
from tools.time_data import TimeData

logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def display_time():
    time_data = TimeData()
    return time_data.get_current_time()

def main():
    try:
        credentials = FileLoader.load_json("config/credentials.json")
        email_details = FileLoader.load_json("config/email_details.json")
        recipients = FileLoader.load_txt("config/recipients.txt")

        sender_email = credentials["email"]
        sender_password = credentials["password"]
        subject = email_details["subject"]
        message = email_details["message"]

        current_time = display_time()

        email_sender = EmailSender(sender_email, sender_password)
        for recipient in recipients:
            try:
                email_sender.send_email(recipient, subject, message)
                logging.info(f"{current_time} - Email sent to {recipient}")
                print(f"{current_time} - Email successfully sent to {recipient}")
            except Exception as e:
                logging.error(f"{current_time} - Failed to send email to {recipient}: {e}")
                print(f"{current_time} - Failed to send email to {recipient}")
    except Exception as e:
        logging.critical(f"{display_time()} - Critical error occurred: {e}")
        print("An error occurred. Check the logs for details.")

if __name__ == "__main__":
    main()
