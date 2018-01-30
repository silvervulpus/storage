import selenium
from selenium import webdriver
driver = webdriver.Firefox()#calls gecko driver
driver.get('http://www.google.com/')#tells firefox what URL to open
driver.maximize_window()
driver.find_element_by_id("lst-ib").send_keys("amish furniture")#uses HTML elemnt ID to find search field, then inputs chosen text ny emulated a keydown emulatedt
driver.find_element_by_name("btnK").click()#finds the search button and emulates a left mouse click
driver.find_element_by_partial_link_text("made").click()#searches for first link with tutorial in the name and emulates a left mouse click
driver.get_screenshot_as_file("./pics/mypic.png")#saves a screen shot to the project folder
driver.quit()#exits firefox and geckodriver




