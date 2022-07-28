import pytest
from selenium import webdriver
from pageObjects.loginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

import time

class Test_001_Login: #In the class name give testcase ID.
    #Create variables
    '''baseURL = "https://admin-demo.nopcommerce.com/"
    username = "admin@yourstore.com"
    password ="admin"'''
    #All these hardcoded values are moved to config.ini file(configurations folder)
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getApplicationUsername()
    password =  ReadConfig.getApplicationPassword()

    logger=LogGen.loggen()   #Logger variable is created.LogGen.loggen() static method is called
# 2 testcases are written for the login screen
    @pytest.mark.regression            #Based on step 11, Grouping Tests
    def test_homePageTitle(self,setUp):
        #self.driver = webdriver.Chrome()
        self.logger.info("********** Test_001_Login **********")
        self.logger.info("********** Verifying Home Page Title **********")
        self.driver = setUp #fixture from conftest file
        self.driver.get(self.baseURL)
        time.sleep(5)
        act_title = self.driver.title
        #self.driver.close()
        if act_title == "Your store. Login":

            assert True
            self.driver.close()
            self.logger.info("********** Home Page Title test is Passed **********")

        else:
            self.driver.save_screenshot(".\\screenshots\\"+"test_homePageTitle.png") # . Dot represents current project directory
            self.driver.close()
            self.logger.error("********** Home Page Title test is Failed **********")
            assert False

    @pytest.mark.sanity           # Based on step 11, Grouping Tests
    @pytest.mark.regression
    def test_login(self,setUp):
        self.logger.info("********** Verifying Login Test **********")
        #self.driver = webdriver.Chrome()
        self.driver = setUp #Whenever we call setUp(fixture) it will return driver
        self.driver.get(self.baseURL)
        #Create object for LoginPage
        self.lp = LoginPage(self.driver)  # __init__(self,driver) is automatically invoked when object lp is created for LoginPage
        # LoginPage constructor is expecting driver as parameter.
        #To access the class variables we have to use self keyword
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)

        self.lp.clickLogin()
        time.sleep(5)

        #After successful login Page title will be different

        act_title = self.driver.title
        #self.driver.close()  #You have to verify only after closing the browser
        if act_title == "Dashboard / nopCommerce administration":

            assert True
            self.driver.close()
            self.logger.info("********** Login Test case Passed **********")
        else:
            self.driver.save_screenshot(".\\screenshots\\"+"test_login.png")
            self.driver.close()
            self.logger.error("********** Login Test case Failed **********")
            assert False


