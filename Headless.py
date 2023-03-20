from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import unittest
from faker import Faker
import time

faker_class = Faker()

fake = Faker()
options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(options=options)

driver.get("https://qasvus.wordpress.com")
driver.maximize_window()
try:
    assert driver.title == "California Real Estate"
except AssertionError:
    print("Title is different.Current title is:", driver.title)
print(driver.current_url)
driver.implicitly_wait(5)

driver.find_element(By.ID, 'send-us-a-message')
driver.find_element(By.ID, 'g2-name').send_keys('Gulya')
driver.find_element(By.ID, 'g2-email').send_keys('Gul@gmail.com')
driver.find_element(By.ID, 'contact-form-comment-g2-message').send_keys('Hello')
driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
time.sleep(3)
driver.find_element(By.CLASS_NAME, 'pushbutton-wide').click()
driver.find_element(By.CLASS_NAME, 'link').click()
button_type = driver.find_element(By.CLASS_NAME, 'pushbutton-wide')
print(type(button_type))
driver.close()