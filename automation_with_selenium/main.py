from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import json

with open('data.json', 'r') as f:
    data = json.load(f)

# driver = webdriver.Chrome()
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get('https://demo.wpeverest.com/user-registration/guest-registration-form/')

# value = driver.find_element(By.ID,'articlecount').find_element(By.TAG_NAME,'a').text
# print(value)

# def data_entry_func(driver,data):
name = driver.find_element(By.NAME,'first_name')
name.send_keys(data['First Name'])

name = driver.find_element(By.NAME,'last_name')
name.send_keys(data['Last Name'])

email = driver.find_element(By.NAME,'user_email')
email.send_keys(data['User Email'])

pass_ = driver.find_element(By.NAME,'user_pass')
pass_.send_keys(data['User Password'])

tnc = driver.find_element(By.ID,'privacy_policy_1665633140')
tnc.click()

submit = driver.find_element(By.TAG_NAME,'button ')
submit.click()


