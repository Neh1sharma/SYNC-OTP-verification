import os
import math
import random
import smtplib

digits = "0123456789"
OTP = ""
for i in range(6):
    OTP+= digits[math.floor(random.random()*10)]
    otp = OTP + "is your OTP"
    msg = otp

s = smtplib.SMTP('smtp.gmail.com',587)  
s.starttls()
s.login("nehapi2024@gmail.com", "obol rozn kzhv xspj")

emailid = input("Please Enter your Email: ")  
s.sendmail('&&&&&&&&&&&&', emailid, msg)

a = input("Please Enter you OTP>>: ")
if a == OTP:
    print("yes, you OYP is Verified")
else:
    print("Please check your OTP Again")
   