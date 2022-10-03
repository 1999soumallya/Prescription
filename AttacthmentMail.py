from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.message import EmailMessage
import smtplib
from Main import speak


# import Main

def sendmail(toaddr, filepath):
    fromaddr = "soumallyadey11@gmail.com"
    # toaddr = "1999gionee@gmail.com"

    msg = EmailMessage()

    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Patient Current Prescription"

    with open(filepath, 'rb') as myfile:
        file_data = myfile.read()
        file_name = myfile.name
        msg.add_attachment(file_data, maintype="application", subtype="pdf", filename=file_name)


    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(fromaddr, "pupundey")
        server.send_message(msg)
    speak('Email Send success Full')
