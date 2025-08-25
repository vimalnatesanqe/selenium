from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser=Service(r"C:\Driver\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=ser)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
import time

driver.find_element(By.XPATH,"//a[normalize-space()='Udemy Courses']").click()
time.sleep(10)
driver.find_element(By.XPATH,"//a[@href='https://www.udemy.com/course/learn-manual-software-testing-with-live-project-jira-tool']").click()
time.sleep(10)
window_id=driver.window_handles
driver.switch_to.window(window_id[1])
driver.find_element(By.LINK_TEXT,"15,001 ratings").click()
driver.switch_to.window(window_id[0])
driver.find_element(By.LINK_TEXT,'Blog').click()
import time
time.sleep(20)

