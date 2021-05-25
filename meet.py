import time
from selenium.webdriver.common.action_chains import ActionChains

class enter_meet:
    def __init__(self, chrome):
        
        self.chrome = chrome
        camera = chrome.find_element_by_xpath('/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[4]/div[2]/div/div/span/span/div/div/svg/g/g/g/g[1]/path')
        ActionChains(self.chrome).move_to_element(camera).perform()
        ActionChains(self.chrome).click(camera).perform()
        sound = chrome.find_element_by_xpath('/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[4]/div[2]/div/div/span/span/div/div/svg/g/g/g/g[1]/path')
        ActionChains(self.chrome).move_to_element(sound).perform()
        ActionChains(self.chrome).click(sound).perform()
        enter = chrome.find_element_by_xpath('/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span/span')
        ActionChains(self.chrome).move_to_element(enter).perform()
        ActionChains(self.chrome).click(enter).perform()
        time.sleep(1)