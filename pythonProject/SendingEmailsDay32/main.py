import smtplib

my_email = "propython23@gmial.com"
Password = "Wan00%@Ds"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=Password)
connection.sendmail(from_addr=my_email, to_addrs="diyohshiloh2@mail.com")
connection.close()