from selenium import webdriver

def headless_mode():
    from selenium.webdriver.chrome.service import Service
    ser_obj=Service(r"C:\Driver\chromedriver-win64\chromedriver.exe")
    ops=webdriver.ChromeOptions()
    ops.headless=True
    driver=webdriver.Chrome(service=ser_obj,options=ops)
    return driver
driver=headless_mode()
driver.get("https://www.dummyticket.com/")
print(driver.title)
print(driver.current_url)

    