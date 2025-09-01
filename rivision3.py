from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests

ser_obj=Service(r"C:\Driver\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)
#implicit wait works based on the time span, once it initiated it will handle through out the program
driver.implicitly_wait(10)


#url
driver.get("https://testautomationpractice.blogspot.com/")

links=driver.find_elements(By.TAG_NAME,'a')
print(len(links))

for i in links:
    url=i.get_attribute('href')
    try:
        res=requests.head(url)
    except:
        print("server error")
    if res.status_code>=400:
        print(url,"this is a broken link")
    else:
        print(url,"this is valid link")