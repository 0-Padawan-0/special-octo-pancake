from selenium import webdriver
from openpyxl import Workbook
import os

from selenium.webdriver.common.by import By

os.environ['PATH'] += r"E:"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.amazon.in/')
driver.implicitly_wait(30)

driver.find_element(By.XPATH, '//*[@id="twotabsearchtextbox"]').send_keys("samsung phones")
driver.find_element(By.XPATH, '//*[@id="nav-search-submit-button"]').click()
driver.find_element(By.XPATH, '//*[@id="p_89/Samsung"]/span/a/span').click()
phonename = driver.find_elements(By.XPATH, '//span[contains(@class,"a-size-medium a-color-base a-text-normal")]')
phoneprice = driver.find_elements(By.XPATH, '//span[contains(@class,"a-price-whole")]')
name = []
price = []
for naam in phonename:
    name.append(naam.text)
for paisa in phoneprice[3:]:
    price.append(paisa.text)
finallist = zip(name, price)
print(len(name))
print(len(price))

wb = Workbook()
sh1 = wb.active
wb['Sheet'].title = "samsung phones"
sh1['A1'].value = "Phone"
sh1['B1'].value = "Price"
for x in list(finallist):
    sh1.append(x)
wb.save("scrapedata.xlsx")
