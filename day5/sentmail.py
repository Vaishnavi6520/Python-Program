# import smtplib
# connection=smtplib.SMTP("smtp.gmail.com",587)
# connection.starttls()
# connection.login("vaishnavi.p6521@gmail.com","Priy@6521")
# message="Hello , I am Vaishnavi"
# connection.sendmail("vaishnavi.p6521@gmail.com", "priya.hajela358@gmail.com", message)
# print("Email sent successfully")
# connection.quit()

import smtplib
li=input("Enter the string")
msg=li[0:6]
#print(msg)
connection=smtplib.SMTP("smtp.gmail.com",587)
connection.starttls()
connection.login("vaishnavi.p6521@gmail.com","Priy@6521")
connection.sendmail("vaishnavi.p6521@gmail.com","priya.hajela358@gmail.com",msg)
print("email has successfully send")
connection.quit()