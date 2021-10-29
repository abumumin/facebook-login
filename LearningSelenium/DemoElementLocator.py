import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class DemoFindElementByID():
    def locate_by_id_demo(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://login.yahoo.com/")
        driver.maximize_window()
        driver.find_element_by_id('login-username').send_keys('twiceabdul')
        time.sleep(1)
        driver.find_element_by_id("login-signin").click()
        time.sleep(1)
        driver.find_element(By.NAME, 'password').send_keys('@Myman1234')
        time.sleep(1)
        driver.find_element_by_id("login-signin").click()

        driver.find_element_by_css_selector("#root_1").click()
        driver.find_element_by_css_selector("a[aria-label='Compose']").click()

        driver.find_element_by_css_selector('#message-to-field').send_keys('abumumin14@gmail.com, abumumin14@outlook.com')
        time.sleep(1)

        driver.find_element_by_css_selector("input[placeholder='Subject']").send_keys('Quality Assurance Engineer')

        time.sleep(5)

        driver.find_element_by_css_selector("div[aria-label='Message body']").send_keys(
            'Hello Hr,<br/> Attached here is my resume. <br/>Best Regards.<br/> Abubakar Mumin')

        time.sleep(5)

        driver.find_element_by_css_selector("button[title='Send this email']").click()

        time.sleep(3)

findbyid = DemoFindElementByID()
findbyid.locate_by_id_demo()

driver.quit()
#findbyid = DemoFindElementByID()
#findbyid.locate_by_id_demo()