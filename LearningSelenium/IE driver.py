from selenium import webdriver
from time import sleep

driver = webdriver.Ie(executable_path="C:\\WebDriver\\IEDriverServer.exe")

driver.get("http://www.facebook.com")
driver.maximize_windows()
sleep(7)
print(driver.title)
driver.close()
