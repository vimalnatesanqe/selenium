from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj=Service(r"C:\Driver\chromedriver-win64\chromedriver.exe")

driver=webdriver.Chrome(service=service_obj)

driver.get("https://omayo.blogspot.com/")

#verify the webpage titile

actual_title='omayo (QAFox.com)'

if actual_title==driver.title:
    print("title test passed")
    print("*"*30)
else:
    print("title test failed")
    print("*"*30)




