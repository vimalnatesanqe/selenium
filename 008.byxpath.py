# There are two type of xpath is available

# 1. absolute xpath
# 2. relative xpath

# 1. Absolute xpath:

# Absolute xpath satrt from the root node (html)###
# and navigae to all the nodes##

# navigation used by /

#example: html/body/div[5]/div[4]/a##########

#this is complex to write and 

########Relative xpath#######
#relative xpath directly jump to the id and after that this is navigate to respective pointer

#it will start from //

# syntax //tagname[@attribute='value']

# there diffrent type of opreator and methods are avaible 

# 1. and
# 2. or
# 3. contains
# 4.starts-with
# 5.text

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service(r"C:\Driver\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("http://www.automationpractice.pl/index.php")

driver.maximize_window()

# using absolute path

# search_box=driver.find_element(By.XPATH,'/html/body/div/div[1]/header/div[3]/div/div/div[2]/form/input[4]')
# search_box.send_keys('shirts')
# search_box=driver.find_element(By.XPATH,'/html/body/div/div[1]/header/div[3]/div/div/div[2]/form/button').click()

# #using relative xpath

# driver.find_element(By.XPATH,"//*[@id='search_query_top']").send_keys("shirt")
# driver.find_element(By.XPATH,"//*[@name='submit_search']").click()

# #using relative xpath and or condition
# driver.find_element(By.XPATH,"//*[@id='search_query_top' or @name='search_query']").send_keys("shirt")
# driver.find_element(By.XPATH,"//*[@name='submit_search' and @type='submit']").click()


#using contains and starts-with function

#contains basically used when the same attribute has dynamic values

#contains is a function, we have to pass two parameters
#syntax
#//tagnae[contains(@id, value)]

#STARTS-WITH
#//TAGNAME[STARTS-WITH(@ATRIBUTE,VALUE)]

#TEXT 
#THIS IS USED FOR INNER TEXT VALUES 
#TAGNAME[TEXT()='TEXT VALUE']


#contains

driver.find_element(By.XPATH,'//input[contains(@class,search_query)]').send_keys("tshirt")

#starts-with
driver.findelement(By.XPATH,'//button[starts-with(@name,submit_)]').click()

#text
driver.findelement(By.XPATH,"//a[text()='Women']").click()





