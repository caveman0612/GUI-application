from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import csv
from mySQL import sendMysql

#__________________________________________________________________________

#### swtiches
headless = True
ticker = "GOOG"

##### turning off headless
if headless == True:
    options = Options()
    options.headless = True
    path = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(path, options=options)
else:
    path = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(path)


website = "https://finance.yahoo.com/quote/" + ticker + "?p=" + ticker + "&.tsrc=fin-srch"
driver.get(website)
full_xpath = "/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[4]/div/div/div/div[3]/div[1]/div/span[1]"


# search = driver.find_element_by_id("yfin-usr-qry")
# search.send_keys(ticker)
# time.sleep(2)

#***************      pressing enter

# search.send_keys(Keys.ENTER)
# time.sleep(1)

#****************       getting current price

current_price = driver.find_element_by_xpath(full_xpath)
print(current_price.text)

#******************  getting local time

localtime = time.asctime( time.localtime(time.time()) )
print(localtime)


# sendMysql(ticker, current_price.text)

#*****************      adding info to CSV

# with open('TSLA.csv', 'a+', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow([ticker, current_price.text, localtime])


driver.quit()
