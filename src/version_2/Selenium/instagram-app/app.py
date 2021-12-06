from selenium import webdriver
from userInfo import username, password
from selenium.webdriver.common.keys import Keys
import time

class Instagram:

    driver_path = "/Users/sadikturan/Drivers/chromedriver"
    # driver_path = "C:\Driver\chromedriver"

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.followers = []

        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages':'en,en_US'})
        self.browser = webdriver.Chrome(Instagram.driver_path, options=self.browserProfile)

    def signIn(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)
        usernameInput = self.browser.find_element_by_name('username')
        passwordInput = self.browser.find_element_by_name('password')

        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)

        passwordInput.send_keys(Keys.ENTER)

        time.sleep(4)

        if self.browser.find_element_by_class_name('cmbtv'):
            el = self.browser.find_element_by_class_name('cmbtv')
            el.find_element_by_tag_name('button').click()

        time.sleep(4)

        if self.browser.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]'):
            self.browser.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()

    def getFollowers(self, max):
        self.browser.get(f"https://www.instagram.com/{self.username}")
        time.sleep(1)
        self.browser.find_element_by_class_name("k9GMp").find_element_by_tag_name("a").click()
        time.sleep(1)

        modal = self.browser.find_element_by_css_selector("div[role=dialog] ul")
        count = len(modal.find_elements_by_tag_name("li"))

        action = webdriver.ActionChains(self.browser)

        print(f"takipçi sayısı: {count}")

        while count<max:
            modal.click()

            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(1)

            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(1)

            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(1)

            newCount = len(modal.find_elements_by_tag_name("li"))

            if count != newCount:
                count = newCount
                print(f"takipçi sayısı: {count}")
                time.sleep(1)
            else:
                break

        i = 0
        followers = modal.find_elements_by_tag_name("li")
        for user in followers:
            link = user.find_element_by_tag_name("a").get_attribute("href")
            self.followers.append(link)
            i += 1
            if i == max:
                break

        self.saveToFile(self.followers)

    def saveToFile(self, followers):
        with open("followers.txt", "w", encoding="UTF-8") as file:
            for user in followers:
                file.write(user + "\n")

    def followUser(self, username):
        self.browser.get(f"https://www.instagram.com/{username}/")
        time.sleep(1)

        followButton = self.browser.find_element_by_tag_name("button")

        if followButton.text == "Follow" or followButton.text == "Follow":
            followButton.click()
            time.sleep(2)
        else:
            print(f"{username} sayfasını zaten takip ediyorsunuz.")

    def followUsers(self, users):
        for user in users:
            self.followUser(user)

    def unFollowUser(self, username):
        self.browser.get(f"https://www.instagram.com/{username}/")

        btn = self.browser.find_element_by_tag_name('button')

        if btn.text == "Message":
            self.browser.find_elements_by_tag_name('button')[1].click()
            time.sleep(2)

            self.browser.find_element_by_css_selector('div[role=dialog] button').click()
        else:
            print(f"{username} sayfasını zaten takip etmiyorsunuz.")

    def unFollowUsers(self, users):
        for user in users:
            self.unFollowUser(user)

    def __del__(self):
        time.sleep(10)
        self.browser.close()

app = Instagram(username, password)

app.signIn()    
# app.followUser('kod_evreni')
# app.followUser('yazilimatolyesi')
app.followUsers(["kod_evreni","yazilimatolyesi"])

# app.unFollowUser('yazilimatolyesi')
# app.unFollowUser('kod_evreni')

app.unFollowUsers(["kod_evreni","yazilimatolyesi"])

app.getFollowers(50)
