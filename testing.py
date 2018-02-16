import selenium, random, time
from selenium.webdriver.support.ui import Select
from selenium import webdriver
lettered = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numericals = ["1","2","3","4","5","6","7","8","9","0"]
for i in range (3):
    name = (random.choice(lettered) + random.choice(lettered) + random.choice(numericals))*3
    years = random.randint(30,70)
    days = random.randint(2,28)
    months = random.randint(2,11)
    driver = webdriver.Firefox()
    driver.get("https://www.roblox.com")
    select = Select(driver.find_element_by_id("MonthDropdown"))
    select.select_by_index(months)
    select = Select(driver.find_element_by_id("DayDropdown"))
    select.select_by_index(days)
    select = Select(driver.find_element_by_id("YearDropdown"))
    select.select_by_index(years)
    driver.find_element_by_id("signup-username").send_keys(name)
    driver.find_element_by_id("signup-password").send_keys("Passworded1")
    driver.find_element_by_id("signup-password-confirm").send_keys("Passworded1")
    driver.find_element_by_id("MaleButton").click()
    driver.find_element_by_id("agreeTermsPrivacyLabel").click()
    driver.find_element_by_id("signup-button").click()
    driver.get_screenshot_as_file("./Desktop/roblox.png")
    time.sleep(7)
    driver.close()
