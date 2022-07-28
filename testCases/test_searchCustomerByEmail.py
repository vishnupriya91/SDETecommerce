import time

import pytest
from selenium import webdriver
from pageObjects.loginPage import LoginPage
from pageObjects.addCustomerPage import AddCustomer
from pageObjects.searchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from selenium.webdriver.common.by import By

class Test_004_SearchCustomerByEmail: #In the class name give testcase ID.
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getApplicationUsername()
    password =  ReadConfig.getApplicationPassword()
    logger=LogGen.loggen()

    @pytest.mark.regression
    def test_addCustomer(self,setUp):
        #self.driver = webdriver.Chrome()
        self.logger.info("********** Test_004_Search Customer By Email **********")
        self.driver = setUp #fixture from conftest file
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("********** Login Successful **********")

        self.logger.info("********** Starting Search Customer By Email **********")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()
        self.logger.info("********** Searching Customer By Email Id **********")
        searchcust = SearchCustomer(self.driver)
        searchcust.setEmail("victoria_victoria@nopCommerce.com")
        searchcust.clickSearch()
        time.sleep(5)
        status=searchcust.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        print(status)
        #assert True == status
        self.logger.info("********** TC_004_SearchCustomer By Email Finished **********")
        #self.driver.close()
