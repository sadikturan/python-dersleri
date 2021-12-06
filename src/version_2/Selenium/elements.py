# https://www.python.org/

{
    0: {'time': '2021-01-13', 'name': 'Python Software Foundation - January 2021 Newsletter'}, 
    1: {'time': '2021-01-12', 'name': '2020 in Review'}, 
    2: {'time': '2021-01-04', 'name': 'Python 3.10.0a4 is now available for testing'}, 
    3: {'time': '2020-12-28', 'name': 'Election Reform Community Update'}, 
    4: {'time': '2020-12-21', 'name': 'Python 3.8.7 is now available'}
}


from selenium import webdriver

chrome_driver_path = "/Users/sadikturan/Drivers/chromedriver"

driver = webdriver.Chrome(chrome_driver_path)

driver.get("https://www.python.org/")

blog_times = driver.find_elements_by_css_selector(".blog-widget time")
blog_names = driver.find_elements_by_css_selector(".blog-widget li a")
blogs = {}

for i in range(len(blog_names)):
    blogs[i] = {
        "time": blog_times[i].text,
        "name": blog_names[i].text
    }

for time in blog_times:
    print(time.text)

for name in blog_names:
    print(name.text)

print(blogs)



driver.close()