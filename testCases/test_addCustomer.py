import pytest
from selenium import webdriver
from pageObjects.loginPage import LoginPage
from pageObjects.addCustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import string
import random

class Test_003_AddCustomer: #In the class name give testcase ID.
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
    @pytest.mark.sanity          #Based on step 11,This line should be inserted above the class name
    def test_addCustomer(self,setUp):
        #self.driver = webdriver.Chrome()
        self.logger.info("********** Test_003_Add Customer **********")
        self.driver = setUp #fixture from conftest file
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("********** Login Successful **********")

        self.logger.info("********** Starting Add Customer Test **********")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()

        self.addcust.clickOnAddNew()

        self.logger.info("********** Providing Customer Info **********")
        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setCustomerRoles("Guests")
        #self.addcust.setManagerOfVendor("Vendor 2")
        self.addcust.setGender("Male")
        self.addcust.setFirstName("Sanjay")
        self.addcust.setLastName("Mithun")
        self.addcust.setDob("11/09/2015")
        self.addcust.setCompany("SBOA")
        self.addcust.setAdminComment("This is for Tesing..........")
        self.addcust.clickOnSave()

        self.logger.info("********** Saving Customer Info **********")

        self.logger.info("********** Add Customer Validation Started **********")

        self.msg = self.driver.find_element(By.TAG_NAME,"body").text
        #all the content in the body tag will be saved in the form of text

        print(self.msg)

        if 'customer has been added successfully.' in self.msg:
            assert True == True
            self.logger.info("********** Add Customer Test Passed **********")
        else:
            self.driver.save_screenshot(".\\screenshots\\"+"test_addCustomer_src.png") # . Dot represents current project directory

            self.logger.error("********** Add Customer Test Passed **********")
            assert True == False

        self.driver.close()
        self.logger.info("********** Ending Add Customer Test **********")

def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))