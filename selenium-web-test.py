from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

import time

username = "admin_vp"
password = "admin_vp"

PATH = r'C:\Users\ferdie\selenium\chromedriver'
driver = webdriver.Chrome(PATH)

driver.get("http://192.168.1.229:8080/vproapp/login")
print(driver.title)

#
#username = driver.find
driver.find_element(By.NAME,"username").send_keys(username)
driver.find_element(By.NAME, "password").send_keys(password)
driver.find_element(By.CSS_SELECTOR, "btn").click()
#driver.quit()