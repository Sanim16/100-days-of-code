##################### Extra Hard Starting Project ######################
import datetime as dt
import pandas
import smtplib
import random

PLACEHOLDER = "[NAME]"
SMTP_SERVER_ADDRESS = "smtp.gmail.com"
PORT = 587
my_email = "" #Your email goes here
my_password = "" #Your password goes here

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
today_date = now.day
today_month = now.month

birthdays = pandas.read_csv("birthdays.csv")
today_birthdays = {
    row["name"]: row.email for (index, row) in birthdays.iterrows() if row.month == today_month and row.day == today_date
}

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
if not today_birthdays:
    pass
else:
    for key, value in today_birthdays.items():
        print(f"Today is {key}'s birthday and their email is {value}")
        letters = ["letter_1", "letter_2", "letter_3"]
        send_letter = random.choice(letters)
        with open(f"letter_templates/{send_letter}.txt") as file:
            email_body = file.read()
        # Perform modifications (replace text)
        modified_content = email_body.replace(PLACEHOLDER, key)

        # # Create the file in write mode
        # with open(f"letter_templates/{key}.txt", "w") as file:
        #     file.write(modified_content)

# 4. Send the letter generated in step 3 to that person's email address.

        with smtplib.SMTP(SMTP_SERVER_ADDRESS, PORT) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=value,
                msg=f"Subject:Happy Birthday {key}\n\n{modified_content}"
            )
