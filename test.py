from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime
from bs4 import BeautifulSoup
import time
import meet

meet_url = 'https://meet.google.com/srb-cygs-kfz'

PASSWD = {
    'user-id':'nonoivan0627@gmail.com',
    'user-pw':'nono0627@!'
}

class login:
    def __init__(self, subject):
        self.subject = subject
        
        # option of the driver
        options = Options()
        options.add_argument("user-data-dir=C:\\Users\\佑丞\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        options.add_experimental_option("prefs", { \
            "profile.default_content_setting_values.media_stream_mic": 1, 
            "profile.default_content_setting_values.media_stream_camera": 1,
            "profile.default_content_setting_values.geolocation": 1, 
            "profile.default_content_setting_values.notifications": 1 
        })
        chrome = webdriver.Chrome(executable_path='./chromedriver', chrome_options=options)
        chrome.get(meet_url)
        meet.enter_meet(chrome)

login('test')