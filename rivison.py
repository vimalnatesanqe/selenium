from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj=Service(r"C:\Driver\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)

#url
driver.get("https://testautomationpractice.blogspot.com/")

#display title
print(driver.title)
#display current url
print(driver.current_url)
#maximized window
driver.maximize_window()

driver.find_element(By.XPATH,"//a[text()='Blog']").click()

#navigational command
driver.back()
driver.forward()
driver.refresh()

#conditonal command
#is enabled
#is displayed
#is selected

search_box=driver.find_element(By.XPATH,"//input[@name='q']")
print("is displayed",search_box.is_displayed())
print("is enabled",search_box.is_enabled())

atribute_value=search_box.get_attribute('class')
print("class -values: ", atribute_value)

search_box.send_keys("selenium4")

#window command
driver.close()
driver.quit()





