from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

ser_obj=Service(r"C:\Driver\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)


driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

drop_down=driver.find_element(By.XPATH,"//select[@id='country']")
drop_down_lis=Select(drop_down)

import time
time.sleep(10)
drop_down_lis.select_by_visible_text("India")
#drop_down_lis.select_by_value('india')
#drop_down_lis.deselect_by_index()

optin_lis=drop_down_lis.options

for i in optin_lis:
    print(i.text)
    if i.text=="Australia":
        i.click()
    else:
        pass


