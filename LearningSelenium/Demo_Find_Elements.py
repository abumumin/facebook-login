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
        driver.find_element_by_id("login-signin").click()

        time.sleep(5)
        #lista = driver.find_elements(By.TAG_NAME, 'input')
        #print(len(lista))
        #for i in lista:
         #   print(i.text)

        driver.find_element(By.NAME, 'password').send_keys('@Myman1234')
        time.sleep(5)
        driver.find_element_by_id("login-signin").click()
        driver.find_element_by_css_selector(".ybar-icon-sprite._yb_1l3r6._yb_192oo").click()
        driver.find_element_by_css_selector("a[aria-label='Compose']").click()

        driver.find_element_by_css_selector('#message-to-field').send_keys('abumumin14@gmail.com')
        time.sleep(3)

        driver.find_element_by_css_selector("input[placeholder='Subject']").send_keys('Quality Assurance Engineer')

        time.sleep(3)

        driver.find_element_by_css_selector("div[aria-label='Message body']").send_keys('Hello Hr, Attached here is my resume. Best Regards. Abubakar Mumin')

        time.sleep(1)

        driver.find_element_by_css_selector("button[title='Send this email']").click()

        time.sleep(2)
findbyid = DemoFindElementByID()
findbyid.locate_by_id_demo()