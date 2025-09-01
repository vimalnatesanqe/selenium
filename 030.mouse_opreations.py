#mouse opreations
#mouse hover
#right click
#double click
#trag and drop

#mouse over

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

ser=Service(r"C:\Driver\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=ser)

driver.get("https://www.copado.com/")

solution=driver.find_element(By.XPATH,'//*[@id="w-dropdown-toggle-1"]/div[1]/div[1]')
product=driver.find_element(By.XPATH,'//*[@id="w-tabs-0-data-w-tab-1"]/div/div')
cicd=driver.find_element(By.XPATH,' //*[@id="w-tabs-0-data-w-pane-1"]/div/div[1]/a[1]/div/div/div')
act=ActionChains(driver)
act.move_to_element(solution).move_to_element(product).move_to_element(cicd).click().perform()

