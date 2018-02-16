import selenium, time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.roblox.com/games/292439477/Phantom-Forces")
time.sleep(2)
driver.find_element_by_id("MultiplayerVisitButton").click()
time.sleep(1)
driver.find_element_by_id("decline-btn").click()
time.sleep(1)
driver.find_element_by_id("Username").send_keys("MyUsername1")
driver.find_element_by_id("Password").send_keys("MyPassword1")
driver.find_element_by_id("signInButtonPanel").click()
time.sleep(2)
driver.find_element_by_id("MultiplayerVisitButton").click()
time.sleep(10)
driver.close()
