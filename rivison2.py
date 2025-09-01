from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj=Service(r"C:\Driver\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)
#implicit wait works based on the time span, once it initiated it will handle through out the program
driver.implicitly_wait(10)


#url
driver.get("https://testautomationpractice.blogspot.com/")

check_box=driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@value,'day')]")
for box in check_box:
    val=box.get_attribute('value')
    print(val)
    if val=="sunday" or "friday":
        box.click()
    else:
        pass
