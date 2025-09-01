from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

ser=Service(r"C:\Driver\chromedriver-win64\chromedriver.exe")

driver=webdriver.Chrome(service=ser)

driver.get("https://testautomationpractice.blogspot.com/")

source=driver.find_element(By.XPATH,'//*[@id="draggable"]')
target=driver.find_element(By.XPATH,'//*[@id="droppable"]')
act=ActionChains(driver)
act.drag_and_drop(source,target).perform()
