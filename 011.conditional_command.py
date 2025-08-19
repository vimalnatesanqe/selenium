from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj=Service(r"C:\Driver\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)

driver.get("https://omayo.blogspot.com/")

#conditional commands works based on the webelement, whether is displayed, is enabled, is selected

#is_displayed
#is_enabled
#is_selected

usr_name_box=driver.find_element(By.XPATH,"//form[@name='form1']/child::input[@type='text']")

print(usr_name_box.is_displayed())
print(usr_name_box.is_enabled())

male_rb=driver.find_element(By.XPATH,"//input[@id='radio1']")
fem_rb=driver.find_element(By.XPATH,"//input[@id='radio2']")

print("before click the radio button status")
print("*"*20)
print(male_rb.is_selected)
print(fem_rb.is_selected)
print("*"*20)
print("after click the radio button status")
male_rb.click()
fem_rb.click()
print(male_rb.is_selected)
print(fem_rb.is_selected)









