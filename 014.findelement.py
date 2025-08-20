from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj=Service(r"C:\Driver\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)

driver.get("https://omayo.blogspot.com/")
driver.maximize_window()

#find element
#find element always return single web element
#even it is pointing multiples  web elements

links=driver.find_element(By.XPATH,"//div[@id='sidebar-left-1']//a")
print(links.text)

