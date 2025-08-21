#there are three type of links
#internal link
#external link
#broken link

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ser_obj=Service(r"C:\Driver\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)
driver.get('https://nallas.com/')
driver.maximize_window()
print(driver.title)
print(driver.current_url)

#access the one link
#driver.find_element(By.LINK_TEXT,"Who We Are").click()

#get all link

all_links=driver.find_elements(By.TAG_NAME,'a')
print("count of all links",len(all_links))

import requests 
count=0
for a_links in all_links:
    #get url value by get atribute
    url=a_links.get_attribute('href')
    try:
        res=requests.head(url)
    except:
        None
    if res.status_code>=400:
        print(url,"this is a broken link")
        count+=1
    else:
        pass
        #print(url,"this is not a broken link")
print("over all link count is", len(all_links))
print("over all broken link count is ", count)




