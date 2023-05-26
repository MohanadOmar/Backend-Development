import time
from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


CHROME_PATH = "C:\\Users\\Mohanad\\OneDrive\\Documents\\chromedriver.exe"
INSTAGRAM_URL = "https://www.instagram.com/"
EMAIL = input("Email: ")
PASSWORD = input("Password: ")
SEARCH_ACCOUNT = input("Enter the targeted account: ")
SCROLL_TIMES = int(input("Enter number from 1-10: "))


class InstagramBot:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_PATH)
        self.driver.get(INSTAGRAM_URL)

    def login(self):
        time.sleep(2)
        user = self.driver.find_element(By.NAME, 'username')
        user.send_keys(EMAIL)
        time.sleep(1)
        password = self.driver.find_element(By.NAME, 'password')
        password.send_keys(PASSWORD)
        time.sleep(2)
        password.send_keys(Keys.ENTER)

    def followers_search(self):
        time.sleep(3)
        self.driver.get(f"{INSTAGRAM_URL}{SEARCH_ACCOUNT}followers/")

        # followers = self.driver.find_element(By.CSS_SELECTOR, 'li a')
        # followers.click()
        time.sleep(2)

        scrollable_popup = self.driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div[2]')
        for i in range(SCROLL_TIMES):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable_popup)
            time.sleep(2)

    def follow(self):
        time.sleep(2)
        follows_list = self.driver.find_elements(By.CSS_SELECTOR, 'li button')
        for button in follows_list:
            try:
                time.sleep(5)
                button.click()
            except ElementClickInterceptedException:
                cancel = self.driver.find_element(By.CSS_SELECTOR, '.aOOlW.HoLwm')
                cancel.click()