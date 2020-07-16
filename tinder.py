from selenium import webdriver
from time import sleep

from login import username, password

a = 0


######################################### Class Tinder ####################################################################

class Tinder():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def tinder_signin(self):

        self.driver.get('https://tinder.com') 
        sleep(5)

################## Comment out these section if fb open directly ###################
        
        more = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/button') 
        more.click()
        sleep(3)
######################################################################################
        
        fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button')
        fb_btn.click()
        

        #  login 
        login = self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])

        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(username)


        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]') 
        pw_in.send_keys(password)

        login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login_btn.click()

        self.driver.switch_to_window(login)

        sleep(10)
        
        popup_1 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]') 
        popup_1.click()

        popup_2 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]') 
        popup_2.click()

        popup_3 = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button') 
        popup_3.click()

    def like_profile(self):
            sleep(2)
            like = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button') 
            like.click()

    def dislike_profile(self):
            sleep(1)
            dislike = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button') 
            dislike.click()


    def superlike_profile(self):
            sleep(2)
            superlike = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[3]/div/div/div/button') 
            superlike.click()

    def nothanks(self):
            sleep(2)
            nothanks_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[3]/button[2]')
            nothanks_btn.click()

    def popupclose(self):
        popup_3 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        popup_3.click()

    def matchclose(self):
        match_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()


    def auto_like_dislike(self):
        global a
        while True:
            sleep(0.5)
            try:
                if (a != 3):
                    a += 1
                    sleep(3)
                    self.like_profile()
                    self.dislike_profile()
                    self.superlike_profile()
                    self.nothanks()
                a = 0
                print("Start again")
            except Exception:
                try:
                    self.popupclose()
                except Exception:
                    self.matchclose()

##################################### Calling Function #############################################################
    
auto = Tinder()
auto.tinder_signin()
auto.auto_like_dislike()

