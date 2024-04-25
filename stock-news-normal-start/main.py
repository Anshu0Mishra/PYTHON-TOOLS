import random
import requests
from datetime import date
from datetime import timedelta
import smtplib
import os

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

# CRYPTO_NAME = "OP"
# CRYPTO_COMPANY_NAME = "OPTIMISM"


STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API = "07I2BO419O7DPXZ1"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API = "5e8e24aecb3341a9bb1e6b850db9d997"

# CRYPTO_ENDPOINT = "https://www.alphavantage.co/query?" \
#                   "function=DIGITAL_CURRENCY_DAILY&" \
#                   "symbol=BTC&" \
#                   "market=INR" \
#                   "&apikey=07I2BO419O7DPXZ1"


# https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol=BTC&market=INR&apikey=07I2BO419O7DPXZ1

# GET https://newsapi.org/v2/everything?q=Tesla Inc&from=2023-07-28&sortBy=popularity&apiKey=5e8e24aecb3341a9bb1e6b850db9d997

today = date.today()
yesterday = today - timedelta(days=1)
day_before_yesterday = today - timedelta(days=2)

my_email = "Email"
passcode = "Password"

news_para = {
    "apiKey": "Api key",
    "qInTitle": COMPANY_NAME
}

# crypto_para = {
#     "function": "DIGITAL_CURRENCY_DAILY",
#     "symbol": CRYPTO_NAME,
#     "market": "INR",
#     "apikey": STOCK_API
# }

stock_para = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API
}

# STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries.
# e.g. [new_value for (key, value) in dictionary.items()]

connection = requests.get(url=STOCK_ENDPOINT, params=stock_para)
data = connection.json()
# print(data)
list_Q = [value for (key, value) in data.items()]
yesterday_closing_stock_price = float(list_Q[1][f'{yesterday}']['4. close'])
# print(yesterday_closing_stock_price)

#TODO 2. - Get the day before yesterday's closing stock price
day_before_yesterday_price = float(list_Q[1][f'{day_before_yesterday}']['4. close'])
# print(day_before_yesterday_price)

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20.
# Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference_between_yesterday_day_before = yesterday_closing_stock_price - day_before_yesterday_price
difference = abs(difference_between_yesterday_day_before).__round__(2)
#
#TODO 4. - Work out the percentage difference in price between closing price yesterday and
# closing price the day before yesterday.
total_half = int((yesterday_closing_stock_price + day_before_yesterday_price) / 2)
percentage_dff = ((difference / total_half) * 100).__round__(2)
print(percentage_dff)
#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if percentage_dff > 3:
    print(f"this difference price gape between yesterday's to before yesterday is {percentage_dff}% \nGet News!")
    # STEP 2: https://newsapi.org/
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
    news_connection = requests.get(NEWS_ENDPOINT, params=news_para)
    articles = news_connection.json()["articles"]
    # print(articles)

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles.
# Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    sliced_articles = articles[slice(0, 3, 1)]


    # STEP 3: Use twilio.com/docs/sms/quickstart/python
    # to send a separate message with each article's title and description to your phone number.

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
    list_of_title_Art = [article["title"] for article in sliced_articles]
    list_of_desc_Art = [article["description"] for article in sliced_articles]



#TODO 9. - Send each article as a separate message via Twilio.
    with smtplib.SMTP("smtp.gmail.com", 587) as connect:
        connect.starttls()
        connect.login(user=my_email, password=passcode)
        connect.sendmail(from_addr=my_email, to_addrs="Emailtosend",
                         msg=f"Subject:In the Stock of {COMPANY_NAME}, there is {percentage_dff}% Fluctuation"
                             f"\n\n There are several news which can demonstrate this\n"
                             f"Title: {list_of_title_Art[random.randint(0, 2)]}\n"
                             f"Description: {list_of_desc_Art[random.randint(0, 2)]}")
