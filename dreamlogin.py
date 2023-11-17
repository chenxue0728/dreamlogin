import time
from selenium import webdriver
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
browser = webdriver.Chrome(options=options)
browser.implicitly_wait(10)
#隐式等待，全局有效，最大等待时间，但不会抛出异常
browser.get('https://open.yunzhijia.com/home/?m=open&a=login')

browser.find_element(By.CLASS_NAME,"login-user").click()

browser.find_element("id","email").send_keys("15330433730")

browser.find_element(By.ID,"password").send_keys("Cx18008671619@")

browser.find_element(By.ID,"log-btn").click()
time.sleep(2)
user = browser.find_element(By.ID,'home-user_name').text
print(user+'已登陆')