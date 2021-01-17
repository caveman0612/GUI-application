from stocktracker.mySQL import *
from stocktracker.webScrapperSelenium import *
from stocktracker.textApplication import *

list = pulltickerandprices()

ticker_list, Target_list = zip(*list)
# print(ticker_list)
# print(Target_list)


# current_price = ScrappingCurrentPrice("TSLA")
# print(type(current_price))
# print(float(current_price))


for index, t in enumerate(ticker_list):

    current_price = ScrappingCurrentPrice(t)
    price = current_price.replace(",", "")

    if float(price) <= float(Target_list[index]):
        sendTextMessage(f"the price of {t} currently is ${price}")
    else:
        sendTextMessage("no major change")


