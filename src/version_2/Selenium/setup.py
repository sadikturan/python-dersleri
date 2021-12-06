from selenium import webdriver

chrome_driver_path = "/Users/sadikturan/Drivers/chromedriver"
# chrome_driver_path = "c:\Drivers"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://sadikturan.com")

driver.close()

