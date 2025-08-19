from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj=Service(r"C:\Driver\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)

driver.get("https://omayo.blogspot.com/")

#App command are used to get app title,url,page soure from the application

#title
#current url
#page source
#get() 

print("*"*20)
print(driver.title)
print("*"*20)
print(driver.current_url)
print("*"*20)
print(driver.page_source)

driver.quit()