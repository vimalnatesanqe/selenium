from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser=Service(r"C:\Driver\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=ser)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

driver.find_element(By.ID,"confirmBtn").click()
confim_alert=driver.switch_to.alert
print(confim_alert.text)
import time
time.sleep(10)
confim_alert.dismiss()
