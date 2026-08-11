#email automation
import random
import math
import smtplib#simple mail transfer protocol library


digits="0123456789"
OTP=""#empty string

for i in range(6):
    OTP+=digits[math.floor(random.random()*10)]
otp=OTP+"is your otp"
msg=otp
s=smtplib.SMTP("smtp.gmail.com",587)
s.starttls()
s.login("tejeswarkothagorla@gmail.com","vznv taul xnpn hayj")
user="tejeswarkothagorla@gmail.com"

emailid=input("enter the mail which you want to send otp")
s.sendmail(user,emailid,msg)

while True:
    a=input("enter the otp")
    if a==OTP:
        print("otp is correct")
    else:
        print("incorrect otp")
