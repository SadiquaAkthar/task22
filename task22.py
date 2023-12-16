#Task to extract the number of followers and following using Absolute Path
# Using Exceptional handling to write Python Selenium codes

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import NoSuchElementException

class Followers_Following:
  
   #constructor
   def __init__(self):
       self.url = "https://www.instagram.com/guviofficial/"
       self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))  

    #To extract the data and print the values
   def login(self):
       try:
            self.driver.get(self.url)
            sleep(2)

            # To extract the data using Absolute Path
            follower_count= self.driver.find_element(by=By.XPATH, value="//button[text()=' followers']").text
            following_count= self.driver.find_element(by=By.XPATH, value="//button[text()=' following']").text
            sleep(2)
       except NoSuchElementException as selenium_error:
            print("Element not found", selenium_error)
       finally: 
            #To print the values
            print(follower_count)
            print(following_count)   
            self.driver.quit() 

FF = Followers_Following()
FF.login()
