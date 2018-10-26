#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 20:50:14 2018

@author: anjalip
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

'''
THIS COMPONENT IS WRITTEN TO EXECUTE IT ON BROWSER SERVER
'''

# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# desired_cap = {
#  'browser': 'Chrome',
#  'browser_version': '69.0',
#  'os': 'OS X',
#  'os_version': 'High Sierra',
#  'resolution': '1920x1080'
# }

# driver = webdriver.Remote(

#     command_executor='http://anjali123:iVUA3bXREjFn71zEpb15@hub.browserstack.com:80/wd/hub',
#     desired_capabilities=desired_cap)

# driver = webdriver.Chrome()

driver.get("https://facebook.com")

time.sleep(2)

username = 'anjali.panwar.friend@gmail.com'
password = 'newpassword@789'

email = driver.find_element_by_name('email')
email.send_keys(username)

time.sleep(2)

pwrd = driver.find_element_by_name('pass')
pwrd.send_keys(password)
pwrd.send_keys(Keys.RETURN)

time.sleep(2)

driver.get('https://www.facebook.com/happyanjie')

text_box = driver.find_element_by_xpath("//textarea[@name='xhpc_message']")
text_box.send_keys("Hello World")
time.sleep(2)

submit = driver.find_element_by_xpath('//*[@id="js_2"]/div[2]/div[3]/div[2]/div/div/span/button')
submit.send_keys(Keys.RETURN)

print("Success")

driver.close() 
