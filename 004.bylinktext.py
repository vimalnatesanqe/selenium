from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj=Service(r"C:\Driver\chromedriver-win64\chromedriver.exe")

driver=webdriver.Chrome(service=ser_obj)

driver.get("https://omayo.blogspot.com/")

#by link text
#link text is case senstive, we should provide full text value for locators

driver.find_element(By.LINK_TEXT,"Page One").click() 

#partial link text

driver.find_element(By.PARTIAL_LINK_TEXT,"page").click()

