from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(executable_path="c:\\WebDriver\\chromedriver.exe")

driver.get("http://www.facebook.com")
driver.maximize_window()
sleep(10)
print(driver.title)
driver.close()
