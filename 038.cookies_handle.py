from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

ser_obj=Service(r"C:\Driver\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)
driver.implicitly_wait(10)
driver.get("https://www.dummyticket.com/")

cookies=driver.get_cookies()
#print(cookies)
print(len(cookies))

for i in cookies:
    print(i.get("domain"))


#we can add,get,delete cookies using the atrribute
#it will store a dictonary form