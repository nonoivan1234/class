from class_ import class_others
from class_ import class_math
from class_ import class_english
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

PASSWD = {
    'user-id':'10930148@sssh.tp.edu.tw',
    'user-pw':'A131892440'
}

class login:
    def __init__(self, subject):
        self.subject = subject
        
        # option of the driver
        options = Options()
        options.add_argument("--disable-notifications")
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        options.add_experimental_option(
            "prefs", {"profile.default_content_setting_values.media_stream_mic": 1, 
            "profile.default_content_setting_values.media_stream_camera": 1,
            "profile.default_content_setting_values.geolocation": 1, 
            "profile.default_content_setting_values.notifications": 1 }
        )
        
        chrome = webdriver.Chrome(executable_path='./chromedriver', chrome_options=options)
        chrome.get('https://accounts.google.com/signin')
        # login page
        chrome.find_element_by_id('identifierId').send_keys(PASSWD['user-id'])
        chrome.find_element_by_xpath('//*[@id="identifierNext"]/div/button').click()
        time.sleep(1.5)
        chrome.find_element_by_name('password').send_keys(PASSWD['user-pw'])
        chrome.find_element_by_xpath('//*[@id="passwordNext"]/div/button').click()
        time.sleep(2)
        
        if self.subject == '數學':
            class_math.math(chrome)
        if self.subject == '英文':
            class_english.english(chrome)
        else:
            class_others.others(self.subject, chrome)
            
if __name__ == '__main__':
    login('英文')