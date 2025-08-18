from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj=Service(r"C:\Driver\chromedriver-win64\chromedriver.exe")

driver=webdriver.Chrome(service=service_obj)

driver.get("https://omayo.blogspot.com/")
driver.maximize_window()
driver.title
list=driver.find_elements(By.TAG_NAME,'a')
print(len(list))

