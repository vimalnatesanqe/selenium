from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj=Service(r"C:\Driver\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)

driver.get("https://www.facebook.com/")

#css selector 3 types

#1. tag and ID -----syntax: tagname#id
#2. tag and classname -----: tagname.classname
#3. tag and attributes-----: tagname[atribute=value]
#4. tag and class and atribute: tagname.classname[aatribute=value]

driver.maximize_window()

#tag and ID
#driver.find_element(By.CSS_SELECTOR,"#alert1").click()

#Tag and classname
# web_e=driver.find_element(By.CSS_SELECTOR,".gsc-input")
# web_e.click()
# import time
# time.sleep(10)

#tag and atributes

#driver.find_element(By.CSS_SELECTOR,"input[name=gender]").click()

#tag and class and atribute

driver.find_element(By.CSS_SELECTOR,".inputtext").send_keys("vimalphonix@gmail.com")
driver.find_element(By.CSS_SELECTOR,"input.inputtext[data-testid=royal-pass]").send_keys("vimaal")
driver.find_element(By.CSS_SELECTOR,"button._42ft[data-testid=royal-login-button]").click()






