from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser=Service(r"C:\Driver\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=ser)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

driver.find_element(By.ID,"promptBtn").click()
prompt_alert=driver.switch_to.alert
prompt_alert.send_keys("welcome vimalathithan")
import time
time.sleep(10)
print(prompt_alert.text)
prompt_alert.accept()