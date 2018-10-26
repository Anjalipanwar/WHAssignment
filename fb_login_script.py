#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 20:50:14 2018

@author: anjalip
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://facebook.com")

time.sleep(2)

username = 'abcd@gmail.com'
password = 'abcd@123'

email = driver.find_element_by_name('email')
email.send_keys(username)

time.sleep(2)

pwrd = driver.find_element_by_name('pass')
pwrd.send_keys(password)
pwrd.send_keys(Keys.RETURN)

time.sleep(2)

print("Hello World")

driver.close()