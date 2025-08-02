import smtplib
import datetime as dt
import random

SMTP_SERVER_ADDRESS = "smtp.gmail.com"
PORT = 587
my_email = "" #Your email goes here
my_password = "" #Your password goes here


now = dt.datetime.now()
day_of_the_week = now.weekday()
if day_of_the_week == 5:
    with open("quotes.txt", "r") as quotes:
        list_of_quotes = [quote.strip() for quote in quotes.readlines()]
        daily_quote = random.choice(list_of_quotes)
    with smtplib.SMTP(SMTP_SERVER_ADDRESS, PORT) as quote_connection:
        quote_connection.starttls()
        quote_connection.login(user=my_email, password=my_password)
        quote_connection.sendmail(
            from_addr=my_email,
            to_addrs="potedah624@percyfx.com", # temporary email address used for testing
            msg=f"Subject:Daily Motivation\n\n{daily_quote}"
        )
