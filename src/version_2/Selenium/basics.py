from selenium import webdriver
import time

chrome_driver_path = "/Users/sadikturan/Drivers/chromedriver"

driver = webdriver.Chrome(chrome_driver_path)

url="https://github.com/"

driver.get(url)

time.sleep(2)
driver.maximize_window()
driver.save_screenshot("github.png")

time.sleep(2)

driver.get(url + "sadikturan")

if "sadikturan" in driver.title:
    driver.save_screenshot("github-sadikturan.png")

print(driver.title)

time.sleep(2)

driver.back()
time.sleep(2)
driver.forward()

driver.close()