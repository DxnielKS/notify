"""Sends an email"""
import smtplib
info = open("details.key","r+")
data=info.readlines()
try:
    username, password = data[0],data[1]
except:
    print("Login details are not entered correctly!")
    quit()
def notify(body="Untitled Body",contact="danielsaisani@gmail.com",subject="Untitled Subject"):
    try:
        server = smtplib.SMTP("smtp.gmail.com:587")
        server.ehlo()
        server.starttls()
        server.login(username,password)
    except:
        print("[!] Connection to email sever was not established!")
        return False
    message = "Subject:"+subject+"\n\n"+body
    server.sendmail(username,contact,message)
    return True