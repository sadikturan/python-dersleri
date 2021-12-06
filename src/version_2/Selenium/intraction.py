from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "/Users/sadikturan/Drivers/chromedriver"

driver = webdriver.Chrome(chrome_driver_path)

driver.get("https://tr.wikipedia.org/wiki/Anasayfa")

articleCountbtn = driver.find_elements_by_css_selector("#articlecount a")[1]
tumPortallar = driver.find_element_by_link_text("Tüm portaller")

# tumPortallar.click()

# searchInput = driver.find_element_by_name("search")
# searchInput.send_keys("Python")
# searchInput.send_keys(Keys.ENTER)

login = driver.find_element_by_css_selector("#pt-login a")
login.click()

time.sleep(3)

username = driver.find_element_by_id("wpName1")
username.send_keys("Sadikturan")

password = driver.find_element_by_id("wpPassword1")
password.send_keys("")

remember = driver.find_element_by_id("wpRemember")
remember.click()

btn = driver.find_element_by_id("wpLoginAttempt")
btn.click()


