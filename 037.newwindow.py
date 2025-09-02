from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

ser_obj=Service(r"C:\Driver\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)
driver.implicitly_wait(10)
driver.get("https://www.dummyticket.com/")

# action=Keys.CONTROL+Keys.RETURN
# driver.find_element(By.XPATH,"").send_keys(action)
driver.switch_to.new_window()

driver.get("https://www.nallas.com/")







