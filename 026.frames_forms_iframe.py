#Switch to frame

#using of frame id or name or index values we can switch one frame to another frame

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser=Service(r"C:\Driver\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=ser)

driver.get("https://omayo.blogspot.com/")
driver.maximize_window()

driver.switch_to.frame('iframe1')
driver.find_element(By.XPATH,'//div[@class="widget-content"]//a').click()
driver.switch_to.default_content()
driver.switch_to.frame('iframe2')
driver.find_element(By.LINK_TEXT,'>> Contact Me').click()
import time
time.sleep(20)

driver.close()



