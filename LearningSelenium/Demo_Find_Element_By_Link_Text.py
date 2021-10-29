import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class DemoFindElementByID():
    def locate_by_id_demo(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://login.yahoo.com/")
        driver.find_element_by_link_text("Help").click()
        time.sleep(3)
findbyid = DemoFindElementByID()
findbyid.locate_by_id_demo()