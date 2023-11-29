import smtplib
import imghdr
from email.message import EmailMessage
from random import randrange


def SendEmail(email):


  EMAIL_ADDRESS ="asem.b0611@gmail.com"
  EMAIL_PASSWORD = "ysyt ympu cqee iqbq"
  RandomCod=randrange(1000,9999)

  msg = EmailMessage()
  msg['Subject'] = f'Verification code {RandomCod}'
  msg['From'] = EMAIL_ADDRESS
  msg['To'] = email

  msg.set_content('This is a plain text email')

  msg.add_alternative(f"""\
  <!DOCTYPE html>
  <html>
      <body>
          <h1 style="color: red;" >Checking for test</h1>
          <h2 style="color:red;">Your code is :{RandomCod}</h2>
      </body>
  </html>
  """, subtype='html')


  with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
      smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
      smtp.send_message(msg)


  return RandomCod