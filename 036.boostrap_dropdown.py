from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj=Service(r"C:\Driver\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)
driver.implicitly_wait(10)
driver.get("https://www.dummyticket.com/")
driver.find_element(By.LINK_TEXT,"Buy Ticket").click()
driver.find_element(By.XPATH,"//span[@id='select2-billing_country-container']").click()
country=driver.find_elements(By.XPATH,"//ul[@id='select2-billing_state-results']//li")
for ctry in country:
    if ctry.text=='India':
        ctry.click()

import os

driver.save_screenshot(os.getcwd()+"//tckt.png")
