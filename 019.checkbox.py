from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ser_obj=Service(r"C:\Driver\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)

#check box
#single element selection
driver.get("https://testautomationpractice.blogspot.com/")
# single_we=driver.find_element(By.ID,"sunday")
# single_we.click()
# single_we.is_displayed()
# print(
#     "Displayed:", single_we.is_displayed(),
#     "Enabled:", single_we.is_enabled(),
#     "Selected:", single_we.is_selected(),
#     "ID Attribute:", single_we.get_attribute("id"),
#     "Text:", single_we.text
# )

#select all check box using loop

checkbox_all=driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
print(len(checkbox_all))

#select all 
# for checkbox in checkbox_all:
#     checkbox.click()

#select last 2
import time
# for checkbox in range(len(checkbox_all)-2,len(checkbox_all)):
#     time.sleep(10)
#     checkbox_all[checkbox].click()

#use contional commands

for checkbox in checkbox_all:
    checkbox.click()
for check in checkbox_all:
    print(check.is_displayed)
    print(check.is_enabled)
    print(check.is_selected)
    print(check.get_attribute(id))
    time.sleep(10)
    check.click()

    
