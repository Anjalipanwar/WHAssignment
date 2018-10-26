#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 16:02:09 2018

@author: anjalip
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()

#Login

url = 'https://wallethub.com/join/login'

driver.get(url)

driver.implicitly_wait(2)

#login = driver.find_element_by_class_name('login')

gmail = 'official.anjali@gmail.com'
password = 'Testuser@1'

email = driver.find_element_by_name('em')
email.send_keys(gmail)

pass1 = driver.find_element_by_name('pw')
pass1.send_keys(password)

pass1.send_keys(Keys.RETURN)

driver.implicitly_wait(5)

#TASK 1
url = 'https://wallethub.com/profile/test_insurance_company/'

driver.get(url)

driver.implicitly_wait(10)



#TASK 2

element_to_hover_over = driver.find_element_by_xpath('//*[@id="wh-body-inner"]/div[2]/div[3]/span')

hover = ActionChains(driver).move_to_element(element_to_hover_over)
hover.perform()

print("hover done")
driver.implicitly_wait(2)

#CLOSE POP UP
#close_popup = driver.find_element_by_class_name('af-icon-cross')
#close_popup.click
#
#print("pop closed")

#driver.implicitly_wait(5)

#TASK 2 - GIVE RATING 

#sel_rating = driver.find_element_by_xpath("//ul[@class='wh-rating rating_4_5']/li[4]/a")

sel_rating = driver.find_element_by_xpath('//*[@id="wh-body-inner"]/div[2]/div[3]/div[1]/div/a[4]')
sel_rating.click()

time.sleep(2)
driver.implicitly_wait(5)


#SELECT DROP DOWN 

health_dropdown = driver.find_element_by_xpath('//*[@id="reviewform"]/div[1]/div/div')
health_dropdown.click()

driver.implicitly_wait(5)

sel_health = driver.find_element_by_xpath('//*[@id="reviewform"]/div[1]/div/ul/li[2]/a')
sel_health.click()


driver.implicitly_wait(2)
print("Selected Health")

driver.implicitly_wait(5)

overall_rating = driver.find_element_by_xpath('//*[@id="overallRating"]/a[5]')
overall_rating.click()

driver.implicitly_wait(5)

content = 'test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test'
text_area = driver.find_element_by_id('review-content')
text_area.send_keys(content)

driver.implicitly_wait(2)

#text_area.send_keys(Keys.RETURN)

#submit = driver.find_element_by_class_name('Submit')
submit = driver.find_element_by_css_selector('#reviewform > div.content > div.submit > input')
submit.click()


print ("Hover Done")



























