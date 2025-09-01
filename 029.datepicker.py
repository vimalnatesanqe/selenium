from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser=Service(r"C:\Driver\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=ser)

driver.get("https://jqueryui.com/datepicker/")

driver.switch_to.frame(0)

date=driver.find_element(By.XPATH,"//input[@id='datepicker']")
#date.send_keys("08/21/2025")

mon="May"
dat="23"
yea="2026"
date.click()
while True:
    month=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    year=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text
    print(type(month))
    print(type(year))
    if month==mon and year==yea:
        break;
    else:
        driver.find_element(By.XPATH,'//*[@id="ui-datepicker-div"]/div/a[2]/span').click()

dates=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
for ele in dates:
    if ele.text==dat:
        ele.click()
        break
import time
time.sleep(30)



