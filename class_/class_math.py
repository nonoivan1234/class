from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime
import time
import meet

classroom_url = 'https://classroom.google.com/u/0/w/MzQzNTMwMzkwODky/t/all'
meet_url = 'https://meet.google.com/lookup/dy4lxv3co2?authuser=0&hs=179'

class math:
    def __init__(self, chrome):
        self.chrome = chrome
        self.chrome.get(classroom_url)
        time.sleep(4)
        # attend
        text = self.chrome.find_element_by_xpath('/html/body/div[4]/div/div/main/div/div/div[4]/ol/li[2]/div[2]/div/div/div[3]/ol/li[1]/div/div/div[3]/div[1]/div[1]/span')
        if text.text[4:9] == datetime.now().strftime("%m.%d"):
            ActionChains(self.chrome).move_to_element(text).perform()
            ActionChains(self.chrome).click(text).perform()
            time.sleep(1)
            select = self.chrome.find_element_by_xpath('/html/body/div[4]/div/div/main/div/div/div[4]/ol/li[2]/div[2]/div/div/div[3]/ol/li[1]/div/div[2]/div[1]/div[3]/div/div[2]/span/label[4]/div/div/div[3]/div')
            ActionChains(self.chrome).move_to_element(select).perform()
            ActionChains(self.chrome).click(select).perform()
            handin = self.chrome.find_element_by_xpath('/html/body/div[4]/div/div/main/div/div/div[4]/ol/li[2]/div[2]/div/div/div[3]/ol/li[1]/div/div[2]/div[1]/div[3]/div/div[3]/div[2]/span/span')
            ActionChains(self.chrome).move_to_element(handin).perform()
            ActionChains(self.chrome).click(handin).perform()
            handin_check = self.chrome.find_element_by_xpath('/html/body/div[13]/div/div[2]/div[3]/div[2]/span/span')
            ActionChains(self.chrome).move_to_element(handin_check).perform()
            ActionChains(self.chrome).click(handin_check).perform()
            time.sleep(2)
            
            self.chrome.get(meet_url)
            meet.enter_meet(chrome)