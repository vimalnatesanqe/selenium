
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

ser=Service(r"C:\Driver\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=ser)

driver.get("https://www.w3schools.com/TAgs/tryit.asp?filename=tryhtml5_ev_ondblclick")

driver.switch_to.frame("iframeResult")
dc_ele=driver.find_element(By.XPATH,"//button[normalize-space()='Double-click me']")
act=ActionChains(driver)
act.double_click(dc_ele).perform()



