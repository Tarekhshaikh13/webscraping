from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get('https://en.wikipedia.org/wiki/Main_Page')

value = driver.find_element(By.ID,'articlecount').find_element(By.TAG_NAME,'a').text
# print(value)

search_bar = driver.find_element(By.NAME,'search')
search_bar.send_keys('Doraemon')
search_bar.send_keys(Keys.ENTER)


