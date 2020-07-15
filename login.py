import email, smtplib, ssl
#encoders to provide encodings
from email import encoders
#importing various MIME
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText

#User configuration
mail_content = 'content of the mail'
sender_address = input('Enter your mail id: ')
sender_pass = input('Enter your password: ')
receiver_address = input('Enter receiver mail id: ')

message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['subject'] = 'subject of the mail'
message.attach(MIMEText(mail_content, 'plain'))

#name of the file to be attach
filename = "***Name of the file***"

#open file for reading
with open(filename, "rb") as attachment:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

#encode into base64
encoders.encode_base64(part)

part.add_header(
        "Content-Disposition",
        f"attachment; filename={filename}",
    )

message.attach(part)
text = message.as_string()

try:
    #create smtp session
    session = smtplib.SMTP('smtp.gmail.com', 587)
    context = ssl.create_default_context()

    #start tls for security
    session.starttls(context=context)

    #authentication
    session.login(sender_address,sender_pass)

    #convert message as string
    text = message.as_string()
    
    #sending mail
    session.sendmail(sender_address,receiver_address,text)

except Exception as e:
    print("something is wrong")

finally: 
    print("closing the server")

session.quit()