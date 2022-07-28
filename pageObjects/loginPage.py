from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage:
    text_box_username_id = "Email"
    text_box_password_id = "Password"
    button_login_xpath = "//button[@class='button-1 login-button']"
    link_logout_linktext = "Logout"

    def __init__(self,driver):  #Python Constructor.Automatically invoked at the time of object creation.
        self.driver=driver      #initiate our local driver. self.driver is the class variable

    #Action Methods
    def setUserName(self,username):
        self.driver.find_element(By.ID, self.text_box_username_id).clear() #Clear the text box.Previous values may get appenden in datadriven testing
        self.driver.find_element(By.ID,self.text_box_username_id).send_keys(username)   #text_box_username_id is the variable which belongs to the class.
                                                                                        #so use self keyword

    def setPassword(self, password):
        self.driver.find_element(By.ID,self.text_box_password_id).clear()  # Clear the text box.Previous values may get appenden in datadriven testing
        self.driver.find_element(By.ID, self.text_box_password_id).send_keys(password)  # text_box_username_id is the variable which belongs to the class.
                                                                                        # so use self keyword
    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT, self.link_logout_linktext).click()

