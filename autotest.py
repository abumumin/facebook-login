from selenium import webdriver
from time import sleep

driver = webdriver.Firefox(executable_path="C:\\WebDriver\\geckodriver.exe")

driver.get("http://www.facebook.com")
driver.maximize_window()
sleep(10)
print(driver.title)
driver.close()
