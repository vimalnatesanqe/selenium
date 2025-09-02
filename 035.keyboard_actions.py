from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

ser=Service(r"C:\Driver\chromedriver-win64\chromedriver.exe")

driver=webdriver.Chrome(service=ser)
driver.implicitly_wait(10)
driver.get("https://text-compare.com/")

driver.maximize_window()
driver.find_element(By.XPATH,'//*[@id="inputText1"]').send_keys("Welcome to python")
act=ActionChains(driver)
act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
act.send_keys(Keys.TAB)
act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
