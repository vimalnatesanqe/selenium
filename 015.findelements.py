from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj=Service(r"C:\Driver\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)

driver.get("https://omayo.blogspot.com/")
driver.maximize_window()

#find elements
#find elements always return list object
#if it is pointing single element that time also it will return list object

links=driver.find_elements(By.XPATH,"//div[@id='sidebar-left-1']//a")
print(len(links))

for i in links:
    print(i.text)

