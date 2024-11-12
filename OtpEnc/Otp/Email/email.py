import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from .. import LOGGER



sender_email = "Crypticotp@outlook.com"
sender_password = "cryptic@123"  # Generate an app password from your Outlook account settings




def sendEmail(email_content, for_what, recipient_email):
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = for_what
    message.attach(MIMEText(email_content, "plain"))
    try:
        with smtplib.SMTP("smtp.office365.com", 587) as smtp_server:
            smtp_server.starttls()
            smtp_server.login(sender_email, sender_password)
            smtp_server.sendmail(sender_email, recipient_email, message.as_string())
    except Exception as e:
        LOGGER.error("An error occurred while sending the email:", str(e))
        return False
    else:
        return True
    
