from selenium import webdriver

chrome_driver_path = "/Users/sadikturan/Drivers/chromedriver"

driver = webdriver.Chrome(chrome_driver_path)

driver.get("https://www.n11.com/urun/next-ye-32020kt-32-hd-dahili-uydu-alicili-led-tv-1345332?magaza=bureyonsenin")

title = driver.find_element_by_class_name("proName").text
price = driver.find_element_by_class_name("newPrice").find_element_by_tag_name("ins").text
searchInput = driver.find_element_by_id("searchData").get_attribute("value")
link = driver.find_element_by_xpath('//*[@id="footer"]/div/div[2]/div[2]/div/ul/li[2]/a').get_attribute("href")
logo = driver.find_element_by_css_selector(".logo img").get_attribute("src")
print(title)
print(price)
print(searchInput)
print(link)
print(logo)

driver.close()