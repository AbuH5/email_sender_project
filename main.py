import logging, pyfiglet
from tools.email_sender import EmailSender
from tools.file_loader import FileLoader
from tools.time_data import TimeData
from colorama import Fore, Back, Style, init

init(autoreset=True)

TOOL_NAME = "MailVortex"
TOOL_LOGO = pyfiglet.figlet_format(TOOL_NAME)

GITHUB_ACCOUNT = "https://github.com/AbuH5"

logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def display_time():
    time_data = TimeData()
    return time_data.get_current_time()

def main():
    print(Fore.CYAN + TOOL_LOGO)
    print(Fore.GREEN + f"{TOOL_NAME} is running...\n")

    print(Fore.YELLOW + f"Check out the GitHub repository: {GITHUB_ACCOUNT}\n")

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
                print(Fore.GREEN + f"{current_time} - Email successfully sent to {recipient}")
            except Exception as e:
                logging.error(f"{current_time} - Failed to send email to {recipient}: {e}")
                print(Fore.RED + f"{current_time} - Failed to send email to {recipient}")
    except Exception as e:
        logging.critical(f"{display_time()} - Critical error occurred: {e}")
        print(Fore.RED + "An error occurred. Check the logs for details.")

if __name__ == "__main__":
    main()
