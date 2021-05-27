from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime
import time

classroom_url = 'https://classroom.google.com/u/1/c/MTk4OTc4NzY4MTMz'

log = open('log.txt', 'r+', encoding='utf-8')
class english:
    def __init__(self, chrome):
        self.chrome = chrome
        self.chrome.get(classroom_url)
        time.sleep(7)
        
        text = self.chrome.find_element_by_xpath('/html/body/div[4]/div[1]/div/div[2]/main/section/div/div[2]/div[2]/div[1]/div[2]/div[1]/html-blob/span')
        try:
            if text.text[:4] == datetime.now().strftime("%m/%d").replace('0', ''):
                send_text = self.chrome.find_element_by_xpath('/html/body/div[4]/div[1]/div/div[2]/main/section/div/div[2]/div[2]/div[2]/div/div[3]/div/div[2]/div[1]/div/div/div[2]')
                send_text.send_keys('已看完')
                time.sleep(2)
                send_btn = self.chrome.find_element_by_xpath('/html/body/div[4]/div[1]/div/div[2]/main/section/div/div[2]/div[2]/div[2]/div/div[3]/div/div[2]/div[2]/div/span/span/svg')
                ActionChains.move_to_element(send_btn).perform()
                ActionChains.click(send_btn).perform()
                log.write(str(datetime.now())+' Successfuly running class_english\n')
                time.sleep(5)
        except :
            log.write(str(datetime.now())+' Error when running class_english\n')