from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

ser_obj=Service(r"C:\Driver\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)


driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

driver.find_element(By.XPATH,"//button[@id='promptBtn']").click()

alrt=driver.switch_to.alert
print(alrt.text)
import time
time.sleep(5)
alrt.send_keys("VIMALATHITHAN")
time.sleep(10)
alrt.accept()
alrt.dismiss()