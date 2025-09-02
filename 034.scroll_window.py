from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

ser=Service(r"C:\Driver\chromedriver-win64\chromedriver.exe")

driver=webdriver.Chrome(service=ser)

driver.get("https://testautomationpractice.blogspot.com/")

driver.maximize_window()

#scroll option we have to use excute class

#driver.execute_script("window.scrollBy(0,3000)","")
import time
time.sleep(10)
flag=driver.find_element(By.XPATH,'//*[@id="HTML7"]/div[1]/p/label')
time.sleep(10)
driver.execute_script("arguments[0].scrolliIntoView();",flag)
time.sleep(10)
