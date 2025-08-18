from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # Correct class name is Service
from selenium.webdriver.common.by import By # by class 

service_obj = Service(r"C:\Driver\chromedriver-win64\chromedriver.exe") 

#launch driver
driver = webdriver.Chrome(service=service_obj)  # Capital 'C' in Chrome and pass 'service' as keyword

#navigate the url
driver.get("https://omayo.blogspot.com/")

#maximized the window
driver.maximize_window()



#Find element by id and clear the box and pass the value
text_box=driver.find_element(By.ID,'textbox1')
text_box.click()
text_box.clear()
text_box.send_keys("vimal")