from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

ser_obj=Service(r"C:\Driver\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)

driver.get("https://omayo.blogspot.com/")

#forward
#back
#refresh

time.sleep(5)
driver.get("https://www.facebook.com/")

driver.back()
time.sleep(5)
driver.forward()
time.sleep(5)
driver.refresh()

