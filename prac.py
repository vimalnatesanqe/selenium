from selenium import webdriver
from selenium.webdriver.chrome.service import Service
class launch():
      
    def launch_md(cls):
    
        ser_obj=Service(r"C:\Driver\chromedriver-win64\chromedriver.exe")
        driver=webdriver.Chrome(service=ser_obj)
        driver.get('https://omayo.blogspot.com/)



