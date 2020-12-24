from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv


#**************** variables ********************************

ticker = "TSLA"
full_xpath = "/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[4]/div/div/div/div[3]/div[1]/div/span[1]"

#********** finding chromdriver

path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path)

#************************     access website

driver.get("https://finance.yahoo.com/")

#*************            searching company

search = driver.find_element_by_id("yfin-usr-qry")
search.send_keys(ticker)
time.sleep(2)

#***************      pressing enter

search.send_keys(Keys.ENTER)
time.sleep(1)

#****************       getting current price

current_price = driver.find_element_by_xpath(full_xpath)
print(current_price.text)

#******************  getting local time

localtime = time.asctime( time.localtime(time.time()) )
print(localtime)

#*****************      adding info to CSV

with open('TSLA.csv', 'a+', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([ticker, current_price.text, localtime])


driver.quit()
