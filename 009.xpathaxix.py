#xpath axis

# 3.ancestor (parent of parent)
# 2.parent node
# 1.self node
# 2.child node
# 3.descantant (child of chile)


# using of self node we can traverse top to bottom or bottom to top 

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service(r"C:\Driver\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://omayo.blogspot.com/")

driver.maximize_window()


text_vadriver.find_element(By.XPATH,"//td[normalize-space()='Kishore']/self::td").text