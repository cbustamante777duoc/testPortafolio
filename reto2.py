import time
import unittest
import warnings
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException


service = Service('C:/drivers/chromedriver.exe')
driver = webdriver.Chrome(service=service)


class PruebaLogin(unittest.TestCase):
    
    def setUp(self):
        self.driver = Service('C:/drivers/chromedriver.exe')
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        warnings.simplefilter('ignore', ResourceWarning)
         
    # creando prueba con username y password incorrectos
    def test_login1(self):
        driver = self.driver
        try:
            driver.get("https://www.saucedemo.com/")
            user_name = driver.find_element(By.XPATH, "//input[contains(@id,'user-name')]")        
            password = driver.find_element(By.XPATH, "//input[contains(@id,'password')]")
            login = driver.find_element(By.XPATH, "//input[contains(@id,'login-button')]")
        
            user_name.send_keys('testing username')
            password.send_keys('testing password')
            login.click()
            time.sleep(1)
            error = driver.find_element(By.XPATH, "//h3[contains(@data-test,'error')]")
            error = error.is_enabled()
            if(error):
                print('los datos son incorrectos')
                print('prueba 1 ok')    
            
        except TimeoutException as ex:
            print(ex.msg)
            print("error"+ex.msg)
    
    # creando prueba poniendo el username en blanco   
    def test_login2(self):
        driver = self.driver
        try:
            driver.get("https://www.saucedemo.com/")
            user_name = driver.find_element(By.XPATH, "//input[contains(@id,'user-name')]")        
            password = driver.find_element(By.XPATH, "//input[contains(@id,'password')]")
            login = driver.find_element(By.XPATH, "//input[contains(@id,'login-button')]")
        
            user_name.send_keys('')
            password.send_keys('testing password')
            login.click()
            time.sleep(1)
            error = driver.find_element(By.XPATH, "//h3[@data-test='error'][contains(.,'Epic sadface: Username is required')]")
            error = error.is_enabled()
            if(error):
                print('falta el username')
                print('prueba 2 ok')    
            
        except TimeoutException as ex:
            print(ex.msg)
            print("error"+ex.msg)
    
    # creando prueba con password en blanco    
    def test_login3(self):
        driver = self.driver
        try:
            driver.get("https://www.saucedemo.com/")
            user_name = driver.find_element(By.XPATH, "//input[contains(@id,'user-name')]")        
            password = driver.find_element(By.XPATH, "//input[contains(@id,'password')]")
            login = driver.find_element(By.XPATH, "//input[contains(@id,'login-button')]")
        
            user_name.send_keys('testing')
            password.send_keys('')
            login.click()
            time.sleep(1)
            error = driver.find_element(By.XPATH, "//h3[@data-test='error'][contains(.,'Epic sadface: Password is required')]")
            error = error.is_enabled()
            if(error):
                print('falta el password')
                print('prueba 3 ok')    
            
        except TimeoutException as ex:
            print(ex.msg)
            print("error"+ex.msg)
    
    # creando prueba con username y password en blanco
    def test_login4(self):
        driver = self.driver
        try:
            driver.get("https://www.saucedemo.com/")
            user_name = driver.find_element(By.XPATH, "//input[contains(@id,'user-name')]")        
            password = driver.find_element(By.XPATH, "//input[contains(@id,'password')]")
            login = driver.find_element(By.XPATH, "//input[contains(@id,'login-button')]")
        
            user_name.send_keys('')
            password.send_keys('')
            login.click()
            time.sleep(1)
            error = driver.find_element(By.XPATH, "//h3[@data-test='error'][contains(.,'Epic sadface: Username is required')]")
            error = error.is_enabled()
            if(error):
                print('falta el username y el password')
                print('prueba 4 ok')    
            
        except TimeoutException as ex:
            print(ex.msg)
            print("error"+ex.msg)
    
    # creando prueba con username y password correctamante
    def test_login5(self):
        driver = self.driver
        try:
            driver.get("https://www.saucedemo.com/")
            user_name = driver.find_element(By.XPATH, "//input[contains(@id,'user-name')]")        
            password = driver.find_element(By.XPATH, "//input[contains(@id,'password')]")
            login = driver.find_element(By.XPATH, "//input[contains(@id,'login-button')]")
        
            user_name.send_keys('standard_user')
            password.send_keys('secret_sauce')
            login.click()
            logo = driver.find_element(By.XPATH, "//div[@class='app_logo'][contains(.,'Swag Labs')]")
            time.sleep(1)
            if(logo.is_enabled()):
                print('prueba 5 ok')
        except TimeoutException as ex:
            print(ex.msg)
            print("error"+ex.msg)
    
    def test_login6(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")

        user_name = driver.find_element(By.XPATH, "//input[contains(@id,'user-name')]")
        password = driver.find_element(By.XPATH, "//input[contains(@id,'password')]")
        login = driver.find_element(By.XPATH, "//input[contains(@id,'login-button')]")

        user_name.send_keys('standard_user')
        password.send_keys('secret_sauce')
        login.click()

        wait = WebDriverWait(driver, 10)
        logo = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='app_logo'][contains(.,'Swag Labs')]")))
        
    
        print('prueba 6 ok')
        

    def tearDown(self):
        driver= self.driver
        driver.close()


if __name__ == "__main__":
    unittest.main()



# referencias
# https://www.geeksforgeeks.org/find_element_by_link_text-driver-method-selenium-python/