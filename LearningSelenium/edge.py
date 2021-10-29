from selenium import webdriver
from time import sleep

driver = webdriver.Edge(executable_path="C:\\WebDriver\\msedgedriver")

driver.get("http://www.facebook.com")
driver.maximize_windows()
sleep(7)
print(driver.title)
driver.close()
