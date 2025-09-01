#wait command
#python time module
#implicit wait  - it works based on the time
#explicit wait - it works based on the condition

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ser_obj=Service(r"C:\Driver\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)
#implicit wait works based on the time span, once it initiated it will handle through out the program
driver.implicitly_wait(10)

#url
driver.get("https://testautomationpractice.blogspot.com/")

driver.find_element(By.XPATH,"//a[text()='Blog']").click()

#explicit wait - it works based on the condition, also it has exception handling
wait=WebDriverWait(driver,10,poll_frequency=3,ignored_exceptions=Exception)
web_ele=wait.until(EC.presence_of_all_elements_located(By.XPATH,"//input[@name='q']"))
web_ele.send_keys("vimal")





