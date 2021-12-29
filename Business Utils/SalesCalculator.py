import re 
import requests
from bs4 import BeautifulSoup

class SalesCalculator:

    url = "https://github.com/Coding-Forest/2022-Store/tree/main/images"
    page = requests.get(url).text

    def __init__(self):
        soup = BeautifulSoup(response, "lxml")
        soup.prettify()

        items = soup.find_all(class_="js-navigation-open Link--primary")

        pattern = "[0-9]+krw"
        sales = []

        for i in items:
            text = i.text
            match = re.findall(pattern, text)
            price = int(re.sub("krw", "", match[0]))
            month = get_month(text)
            print(f"{format_month(month)} {get_date(text)}: {'{:,}'.format(price)}")
            sales.append(price)

        print()
        print("sales total: {:,} KRW".format(sum(sales)))


    def get_month(text):
        return text[4:6]

    def format_month(number):
        return {
            "01": "Jan",
            "02": "Feb",
            "03": "Mar",
            "04": "Apr",
            "05": "May",
            "06": "Jun",
            "07": "Jul",
            "08": "Aug",
            "09": "Sep",
            "10": "Oct",
            "11": "Nov",
            "12": "Dec" 
        }[number]

    def get_date(text):
        return text[6:8]

sc = SalesCalculator()
