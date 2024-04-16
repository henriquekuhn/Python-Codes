from bs4 import BeautifulSoup
import requests
import lxml
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

DIR = os.getcwd() + "/Day 47 - Amazon Price Tracker"
os.chdir(DIR)

MAIL_PROVIDER_SMTP_ADDRESS = os.getenv("MAIL_PROVIDER_SMTP_ADDRESS")
MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")

URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7"
}
response = requests.get(url=URL, headers=header)

soup = BeautifulSoup(response.content, "lxml")
whole_price = soup.find(class_ = "a-price-whole").getText()
decimal_price = soup.find(class_ = "a-price-fraction").getText()

price = float(whole_price + decimal_price)
print(price)

title = soup.find(id="productTitle").get_text().strip()
print(title)

if price < 100:
    message = f"{title} is now {price}"

    with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=MY_EMAIL,
                    msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode("utf-8")
                )
else:
    print("The price still higher.")