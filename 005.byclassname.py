from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj=Service(r"C:\Driver\chromedriver-win64\chromedriver.exe")

driver=webdriver.Chrome(service=ser_obj)

driver.get("https://omayo.blogspot.com/")

#when we go with class name it will return multiple objects
#so we have to use findelements instead of findelement


lis=driver.find_elements(By.CLASS_NAME,"widget-content")

print(len(lis))

