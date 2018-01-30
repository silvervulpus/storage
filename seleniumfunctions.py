"""Pert Plus Selenium WebDriver sub package. Written by Matthew Silvers 1/22/2018 - 1/25/2018 """

import selenium, sys
from selenium import webdriver

def Firefox_get():
    global driver
    driver = webdriver.Firefox()#calls gecko driver
    driver.maximize_window()

def Chrome_get():
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()

def Quitting_Window():
    global ask
    ask = input("Would you like to close your current window? tab 'y' or 'n'. ")
    if ask == 'y':
        driver.quit()
    elif ask == 'n':
        pass
    else:
        Quitting_Window()

def Quitting_All():
    global asking
    asking = input("Would you like to close your current window? tab 'y' or 'n'. ")
    if ask == 'y':
        driver.quit()
        sys.exit()
    elif ask == 'n':
        pass
    else:
        Quitting_All()

def URL_Entry():
    global where
    where = input("Please type in the url for the website you wish to visit. ")
    driver.get('{}'.format (where) )#tells driver what URL to open

def HTML_ID():
    global html_id, message
    html_id = input("Please enter the html ID of the form field you wish to type into. ")
    message = input ("Please enter the information you with to type into the selcted field ")
    driver.find_element_by_id("{}".format(html_id)).send_keys("{}".format(message))

def By_Name_Button():
    global name
    name = input("Please enter the name identifier for the button you wish to press. ")
    driver.find_element_by_name("{}".format(name)).click()#finds the search button and emulates a left mouse click

def By_Partial_Text():
    global partial_text
    partial_text = input("Please type in the information you wish to seek then select. ")
    driver.find_element_by_partial_link_text("{}".format(partial_text)).click()
def Screen_Shots():
    global path_name
    path_name = input ("Please enter the file path and name of the screen shot's save location. ")
    driver.get_screenshot_as_file("{}".format(path_name))#saves a screen shot to the project folder

