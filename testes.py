# Python program to demonstrate 
# selenium 
  
# import webdriver 
from selenium import webdriver 
import chromedriver_binary  # Adds chromedriver binary to path


# create webdriver object 
driver = webdriver.Chrome()
  
# get python.org
driver.get("http://www.python.org")




