"""Jewelosco Coupon Clipper using Selenium
Uses a Selenium web driver Chrome browser to clip Jewelosco coupons. 
Relies on config.yml file for username and password interested catagory. Besides interested catagory , load "Weekly Add Coupon" only for practical purpose
This script heavy and relies on the the css attribute of coupons and their buttons to identify click targets.  As the css changes, this script will need
to be updated.
All of the delay is added intentionly to act like real human as much as possilbe

"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from subprocess import Popen
from time import sleep
from random import random
import yaml


def log_in(chrome):
    chrome.get('https://www.jewelosco.com/account/sign-in.html')
    #Sleep 4 Seconds
    sleep(4)
    #Get uer email and pwd from config file
    with open('config.yml', 'r') as file:
        coupon_config = yaml.safe_load(file)

    account = coupon_config ['userinfo']['email']
    pw = coupon_config ['userinfo']['passowrd']
    file.close()

    #Trying to be looked at as human as possible by adding a randomized delay (e.g. 0.2-0.6 seconds) between typing
    try:
        email = chrome.find_element(By.ID, 'label-email')
        for ch in account :
            n = 0.2 + random() * 0.4
            sleep(n)
            email.send_keys(ch)

        password = chrome.find_element(By.ID, 'label-password')
        for ch in pw:
            n = 0.2 + random() * 0.4
            sleep(n)
            password.send_keys(ch)

        sleep(2)
        submit = chrome.find_element(By.ID, 'btnSignIn')
        submit.click()
    
    except NoSuchElementException:
        pass

    #Sleep 4 Seconds
    sleep(4)

def add_catagory_coupon(keywords,chrome):
    errors = []
    #Go to coupon pages
    chrome.get('https://www.jewelosco.com/foru/coupons-deals.html')

    #Sleep 4 Seconds
    sleep(4)

    #Search interested coupon type
    try:
        keyword = chrome.find_element(By.ID, 'skip-main-content')
        for ch in keywords:
             n = 0.2 + random() * 0.4
             sleep(n)
             keyword.send_keys(ch)
        #Sleep 2 Seconds    
        sleep(2)
        #Click and search for the keywords
        submit = chrome.find_element(By.CSS_SELECTOR,'[class="search-nav__icon searchBtn svg-icon-search-grey"]')
        submit.click()

    except NoSuchElementException:
        pass

    #Sleep 4 Seconds
    sleep(4)

    #Find all searched coupons
    aimcontent = chrome.find_element(By.CLASS_NAME,'coupon-grid-offers')
    aimslist = aimcontent.find_elements(By.XPATH,'coupon-item[@class="col-12 col-sm-12 col-md-6 col-lg-4 coupon-grid-offer"]')

    #Clip coupons
    for index, aim in enumerate(aimslist):
        try:
            #Find new coupon and print out
            clip_ele = aim.find_element(By.CSS_SELECTOR,'[role="button"][class="btn grid-coupon-btn btn-default"]')
            clip_ele.click()
            n = 0.2 + random() * 0.2 #delay a little bit for each coupon
            sleep(n)
            print(f'No.{index+1}coupon is clipped')
        except:
            try:
                #The coupon already been clipped
                check_ele = aim.find_element(By.CSS_SELECTOR,'g[fill-rule="evenodd"]')
                print(f'No.{index+1}coupon is already clipped')
            except:
                #Coupon not found
                print(f'No.{index+1}coupon is not found')
                errors.append(index+1)
    #Print errors            
    if len(errors) != 0:
        print('There are %d errors' % len(errors))

    #Clear Search  result and back to the normal coupon page
    sleep(2)
    submit = chrome.find_element(By.CSS_SELECTOR,'[class="search-nav__icon searchBtn svg-icon-search-Close"]')
    submit.click()

def add_weekly_coupon(chrome):
    #Search Weekly Add Coupon
    errors = []
    sleep(2)
    submit = chrome.find_element(By.CSS_SELECTOR,'[role="checkbox"][aria-label="Event grouping 2 of 2 Weekly Ad Coupons"]')
    submit.click()

    #Find all coupons
    aimcontent = chrome.find_element(By.CLASS_NAME,'coupon-grid-offers')
    aimslist = aimcontent.find_elements(By.XPATH,'coupon-item[@class="col-12 col-sm-12 col-md-6 col-lg-4 coupon-grid-offer"]')

    #Clip coupons
    for index, aim in enumerate(aimslist):
        try:
            clip_ele = aim.find_element(By.CSS_SELECTOR,'[role="button"][class="btn grid-coupon-btn btn-default"]')
            clip_ele.click()
            n = 0.2 + random() * 0.2
            sleep(n)
            print(f'No.{index+1}coupon is clipped')
        except:
            try:
                check_ele = aim.find_element(By.CSS_SELECTOR,'g[fill-rule="evenodd"]')
                print(f'No.{index+1}coupon is already clipped')
            except:
                print(f'No.{index+1}coupon is not found')
                errors.append(index+1)
            
    if len(errors) != 0:
        print('There are %d errors' % len(errors))

if __name__ == "__main__":

    #Reserve Options for feature use purpose 
    options = Options()
    chrome = webdriver.Chrome()

    #Log in to account
    log_in(chrome)

    #Add all of the catagories coupons
    with open('config.yml', 'r') as file:
     coupon_config = yaml.safe_load(file)
     catagory = coupon_config ['catagory']
    
    for keywords in catagory:
        add_catagory_coupon(keywords,chrome)

    #Add  weeily coupons
    add_weekly_coupon(chrome)

    #close website
    chrome.close()


