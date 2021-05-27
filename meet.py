from datetime import datetime
import time
from selenium.webdriver.common.action_chains import ActionChains
log = open('log.txt', 'r+', encoding='utf-8')
class enter_meet:
    def __init__(self, chrome):
        self.chrome = chrome
        try:
            time.sleep(2)
            close = self.chrome.find_element_by_xpath('/html/body/div/div[3]/div/div[2]/div[3]/div/span/span')
            ActionChains(self.chrome).move_to_element(close).perform()
            ActionChains(self.chrome).click(close).perform()
            time.sleep(1)
            enter = self.chrome.find_element_by_xpath('/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span/span')
            ActionChains(self.chrome).move_to_element(enter).perform()
            ActionChains(self.chrome).click(enter).perform()
            time.sleep(10)
            log.write(str(datetime.now())+' Successfuly entering meet\n')
            time.sleep(3600)
        except :
            log.write(str(datetime.now())+' Error when entering meet\n')
        time.sleep(1)