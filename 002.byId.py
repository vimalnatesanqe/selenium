from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # Correct class name is Service
from selenium.webdriver.common.by import By # by class 

service_obj = Service(r"C:\Driver\chromedriver-win64\chromedriver.exe")  # Use raw string for Windows path

driver = webdriver.Chrome(service=service_obj)  # Capital 'C' in Chrome and pass 'service' as keyword

driver.get("https://omayo.blogspot.com/")
driver.maximize_window()
driver.find_element(By.ID,'textbox1').click().clear().sendkeys("vimal")