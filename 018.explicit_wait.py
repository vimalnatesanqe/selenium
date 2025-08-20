#Explicit wait works based on the condition
#we no need to use find elements 
#Explicit wait untill the web element is avaialable
#we can handle exceptions, if it is throww error paralely other line will be exceute.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

ser_obj=Service(r"C:\Driver\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)

wait=WebDriverWait(driver,10)
# driver.get("https://www.selenium.dev/")
# web_ele=driver.find_element(By.XPATH,"//img[@title='BrowserStack']")
# web_ele.click()
# web_ele=driver.find_element(By.XPATH,"//button[@aria-label='Get a Demo']").click()

# web_ele=wait.until(EC.presence_of_element_located(By.XPATH,"//textarea[@id='APjFqb']"))
# web_ele.send_keys("Selenium")
# web_ele.submit()

#also we can use this one is as exception handling

wait=WebDriverWait(driver,10,poll_frequency=2,ignored_exceptions=Exception)


#driver
#10 - Waiting time
#poll_frequency=2 it will check every 2 sec
#ignored exceptions -- exception handling

w_e=wait.until(EC.presence_of_element_located(By.XPATH,""))



