import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class DemoFindElementByID():
    def locate_by_id_demo(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://login.yahoo.com/")
        driver.maximize_window()
        #driver.find_element_by_link_text("Help").click()
        driver.find_element(By.ID, 'login-username').send_keys('twiceabdul')
        driver.find_element_by_link_text("Help").click()
        time.sleep(5)
        driver.minimize_window()
        driver.quit()
findbyid = DemoFindElementByID()
findbyid.locate_by_id_demo()