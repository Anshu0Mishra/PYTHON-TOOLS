import smtplib
import pandas
import datetime as dt

email = "EMAIL"
passcode = "PASSWORD"
now = dt.datetime.now()
month = now.month
day = now.day
data = pandas.read_csv("birthdays.csv")
birthdate = {(row["month"], row["day"]): row for (index, row) in data.iterrows()}
current_date = (month, day)
if current_date in birthdate:
    birthdate_person = birthdate[current_date]
    my_gmail = email
    my_pass = passcode
    with open("letter_templates/letter_2.txt") as letter:
        content = letter.read()
        content_modified = content.replace('[NAME]', birthdate_person["name"])
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_gmail, password=my_pass)
        connection.sendmail(from_addr=my_gmail, to_addrs=birthdate_person["email"],
                            msg=f"Subject:Happy Birthday!\n\n"f"{content_modified}")
