
import smtplib

sender_email = "aniketsingh9920932616@gmail.com"
rec_email = "aniketsingh9920932616@gmail.com"
password = input(str("Please enter your password : "))
message = "Hey, this was sent using python"

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

n=int(input("enter 2+3"))#doing this just for catpcha(BTW it will be added)
if n==5:
    server.login(sender_email, password)
    print("Login success")
    server.sendmail(sender_email, rec_email, message)
    print("Email has been sent to ", rec_email)
else:
    print("noob")
