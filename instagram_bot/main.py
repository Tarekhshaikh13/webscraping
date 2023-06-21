from selenium import webdriver
from InstaFollower import InstaFollower
from credentials import USERNAME,PASS
import time

options = webdriver.ChromeOptions().add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)

if __name__ == "__main__":
    bot = InstaFollower(USERNAME,PASS,driver)
    bot.login()
    bot.find_followers('chefsteps')
    time.sleep(100)