from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

ser=Service(r"C:\Driver\chromedriver-win64\chromedriver.exe")

driver=webdriver.Chrome(service=ser)

driver.get("https://testautomationpractice.blogspot.com/")

driver.maximize_window()

min_value=driver.find_element(By.XPATH,'//*[@id="slider-range"]/span[1]')
max_value=driver.find_element(By.XPATH,'//*[@id="slider-range"]/span[2]')
print(min_value.location)
print(max_value.location)

act=ActionChains(driver)
import time
time.sleep(10)
act.drag_and_drop_by_offset(min_value,-800,0)
time.sleep(10)
act.drag_and_drop_by_offset(max_value,-1500,0)
time.sleep(10)

print(min_value.location)
print(max_value.location)

driver.execute_script("")