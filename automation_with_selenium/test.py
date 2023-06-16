from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime


# Create a new ChromeDriver instance
driver = webdriver.Chrome()
driver.get('https://www.python.org/')


events = driver.find_element(By.CLASS_NAME,'medium-widget.event-widget.last')
events = events.find_elements(By.TAG_NAME,'li')
time_event ={}

for i in range(len(events)):

    date_time = events[i].find_element(By.TAG_NAME,'time').get_attribute('datetime')
    date = datetime.fromisoformat(date_time).strftime('%Y-%m-%d')
    event = events[i].find_element(By.TAG_NAME,'a').text
    
    time_event[i]={'name':event,'date':date}

print(time_event)