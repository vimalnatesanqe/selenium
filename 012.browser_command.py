from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj=Service(r"C:\Driver\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)

driver.get("https://omayo.blogspot.com/")

#browser command
#close = it will close single window which is pointing the start window

#quit = it will close all the window, which is kill currnet driver


driver.close()
driver.quit()