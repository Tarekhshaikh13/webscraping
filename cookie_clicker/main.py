from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)

driver = webdriver.Chrome(options=options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

click_button = driver.find_element(By.ID,'cookie')

store = driver.find_element(By.ID,'store')
items = store.find_elements(By.CLASS_NAME,'grayed')

items.pop() #last element is empty


# for item in reversed(items):max_val.append(int(item.find_element(By.TAG_NAME,'b').text.split()[-1].replace(",","")))
def max_item_purchase():
    for item in reversed(items):
        # print(item.text)
        item_money_element = item.find_element(By.TAG_NAME,'b').text
        item_money = int(item_money_element.split()[-1].replace(",",""))
        money = int(driver.find_element(By.ID,"money").text)
        if money>item_money:
            item.click()
# max_item_purchase()
while True:
    click_button.click()
    max_item_purchase()

driver.quit()