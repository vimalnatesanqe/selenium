from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj=Service(r"C:\Driver\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)

driver.get("https://omayo.blogspot.com/")
driver.maximize_window()

#text is a predefined selinum keyword
#using of this keyword we can get inner text values from web element
#a tag always contain inner text

links=driver.find_elements(By.XPATH,"//div[@id='sidebar-left-1']//a")
print(len(links))

for i in links:
    print(i.text)

#get atribute
#get atribute is a function using of this we can get value of the atribute values


links=driver.find_element(By.XPATH,"//button[normalize-space()='LogIn']")

print(links.get_attribute('type'))
print(links.get_attribute('value'))


links=driver.find_element(By.XPATH,"//input[@id='textbox1']")

print(links.get_attribute('name'))
print(links.get_attribute('value'))



