from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#service object for driver init
ser_obj=Service(r"C:\Driver\chromedriver-win64\chromedriver.exe")

#driver launch
driver = webdriver.Chrome(service=ser_obj)

#navigate to url
driver.get("https://omayo.blogspot.com/")

#maximized window
driver.maximize_window()

#capture the title
title_name=driver.title
print(f"the title name is {title_name}")

text_box=driver.find_element(By.NAME,"fname")
text_box.click()
text_box.clear()
text_box.send_keys("vimalathithan Natesan")


