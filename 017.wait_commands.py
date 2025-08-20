# wait commands three types
#python method time.sleep(ms)
#implicitly wait(ms)
#explicitwait

#python time.sleep()

# it will reduce the performance
#also it will throw the exception error when the webelement not available


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

ser_obj=Service(r"C:\Driver\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)
driver.implicitly_wait(10) #implicit wait declare

driver.get("https://omayo.blogspot.com/")
time.sleep(10)
driver.maximize_window()


#implicit wait
#easy to declare
#once it is declared below driver instance it will exceute full pprogram
