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


# chrome_driver = os.getcwd() +"/chromedriver"

'''
CONFIG/LOGIN DETAIL
'''

BASE_URL = "https://wallethub.com/join/login"

DEFAULT_USER_ID = "official.anjali@gmail.com"

DEFAULT_PASSWORD = "Testuser@1"

INSURANCE_PAGE_URL = 'https://wallethub.com/profile/test_insurance_company/'


driver = webdriver.Chrome()

'''
THIS METHOD IS WRITTEN TO HANDLE POP UP WIDGET WHICH APPEARS ON INSURANCE PAGE
'''
def handle_popup():
    #This method is written to close pop up which opens suddenly
    print("Verifying if the pop up is Open")
    try:
        	popup = driver.find_element_by_xpath('//*[@id="footer_cta"]/span/span/i[2]')
        	popup.click()
    except:
        	pass
        
'''
THIS METHOD CONTAINS THE ACTUAL CODE WHERE ALL THE MENTIONED STEPS IN THE ASSIGNMENT IS PERFORMED
'''
    
def actionsonInsurancePage():  
    try:
        #LOGIN INTO WALLETHUB USER ACCOUNT
        driver.get(BASE_URL)
        driver.implicitly_wait(2)
        
        #Enter email Id
        email = driver.find_element_by_name('em')
        email.send_keys(DEFAULT_USER_ID)
        
        #Enter Password
        pass1 = driver.find_element_by_name('pw')
        pass1.send_keys(DEFAULT_PASSWORD)
        
        #Enter
        pass1.send_keys(Keys.RETURN)
        driver.implicitly_wait(5)

        print("Login Successful")
    
        #NAVIGATE TO INSURANCE PAGE
        driver.get(INSURANCE_PAGE_URL)
        driver.implicitly_wait(10)
        
        #HOVER ON THE RATINGS
        element_to_hover_over = driver.find_element_by_xpath('//*[@id="wh-body-inner"]/div[2]/div[3]/span')
        hover = ActionChains(driver).move_to_element(element_to_hover_over)
        hover.perform()
        driver.implicitly_wait(2)
        
        #SELECT STAR TO GIVE 4 RATING
        sel_rating = driver.find_element_by_xpath('//*[@id="wh-body-inner"]/div[2]/div[3]/div[1]/div/a[4]')
        sel_rating.click()
        
        time.sleep(2)
        print("Gave 4 star rating Successfully")
    
        #SELECT DROP DOWN 
        health_dropdown = driver.find_element_by_xpath('//*[@id="reviewform"]/div[1]/div/div')
        health_dropdown.click()
    
        #CLICK ON THE HEALTH OPTION
        sel_health = driver.find_element_by_xpath('//*[@id="reviewform"]/div[1]/div/ul/li[2]/a')
        
        #Close pop up 
        handle_popup()
        sel_health.click()

        print("Health option selected Successfully from the drop down")
    
        # driver.implicitly_wait(5)
    
        #Close pop up 
        handle_popup()
        driver.implicitly_wait(7)
        
        #GIVE 5 STAR RATING
        overall_rating = driver.find_element_by_xpath('//*[@id="overallRating"]/a[5]')
        overall_rating.click()

        #Close pop up 
        handle_popup()
        driver.implicitly_wait(5)

        print("Gave 5 star rating Successfully")
        
        #ENTER TEXT IN THE REVIEW BOX
        content = 'I am posting test Review content. test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test'
        text_area = driver.find_element_by_id('review-content')
        
        #CLEARS THE EXISTING CONTENT IF THERE IS ANY IN THE THE REVIEW BOX
        text_area.clear()

        #Close pop up 
        handle_popup()

        #WRITE THE REVIEW CONTENT IN THE REVIEW BOX
        text_area.send_keys(content)
    
    	#Close pop up 
        handle_popup()

        submit = driver.find_element_by_css_selector('#reviewform > div.content > div.submit > input')
    	
    	#Close pop up 
        handle_popup()

        #CLICK SUBMIT
        submit.click()

        print ("Review content submitted Successfully")

        driver.implicitly_wait(2)
    
    	#Hover on Profile
        profile_hover = driver.find_element_by_xpath('//*[@id="viewport"]/header/div/nav[3]/div[1]/a[9]')
        hover = ActionChains(driver).move_to_element(profile_hover)
        hover.perform()
        driver.implicitly_wait(2)
        click_profile = driver.find_element_by_xpath('//*[@id="m-user"]/ul/li[1]/a')

        #CLICK ON PROFILE
        click_profile.click()
        driver.implicitly_wait(2)
        box = driver.find_element_by_class_name('feeddesc')
    
        txt = box.text 
        print('txt--->',txt)
        print('content--->',content)

        #VALIDATE IF THE REVIEW IS AVAILABLE ON PROFILE PAGE 
        try:
            assert content == txt
            print("CONTENT MACTHED : REVIEW IS AVAILABLE ON PROFILE PAGE")
        except:
            print("Failure : : REVIEW IS NOT AVAILABLE ON PROFILE PAGE")

    except Exception as ex:
        print ('Error occured: ',str(ex))



actionsonInsurancePage()


driver.quit()
