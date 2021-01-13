import smtplib
from email.mime.text import  MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def send(filename):
    from_ = "san.singh39@gmail.com"
    to_ = "codersan9@gmail.com"
    subject = "Finance Stock Report"
    body = "Today's Finance Stock Report"

    msg = MIMEMultipart()
    msg['From'] = from_
    msg['To'] = to_
    msg['Subject'] = subject
    msg.attach(MIMEText(body,"plain"))


    #Attaching the file
    my_file = open(filename, 'rb')
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((my_file).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename= ' + filename)
    msg.attach(part)

    message = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_, 'wcvnmjxhbxoqtltb')
    server.sendmail(from_, to_, message)

    server.quit()
