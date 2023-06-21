from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class InstaFollower:
    def __init__(self,name,pass_,driver):
        self.name = name
        self.pass_ = pass_
        self.driver = driver

    def login(self):
        self.driver.get("https://www.instagram.com")
        time.sleep(5)
        name_box= self.driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input')
        name_box.send_keys(self.name)

        time.sleep(2)
        pass_box = self.driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input')
        pass_box.send_keys(self.pass_)
        time.sleep(2)

        submit = self.driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]/button')
        submit.click()
        time.sleep(5)
    def find_followers(self,account_name):
        self.driver.get(f"https://www.instagram.com/{account_name}/")
        time.sleep(7)
        follow_button =self.driver.find_element(By.PARTIAL_LINK_TEXT,' followers')
        follow_button.click()
    def follow():
        pass






