from selenium import webdriver
from time import sleep

driver = webdriver.Opera(executable_path="C:\\WebDriver\\operadriver.exe")

driver.get("http://www.facebook.com")
driver.maximize_window()
sleep(7)
print(driver.title)
driver.close()

