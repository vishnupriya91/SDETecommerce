import pytest
from selenium import webdriver
from pageObjects.loginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
import time

class Test_002_DDT_Login: #In the class name give testcase ID.

    #Create variables
    '''baseURL = "https://admin-demo.nopcommerce.com/"
    username = "admin@yourstore.com"
    password ="admin"'''
    #All these hardcoded values are moved to config.ini file(configurations folder)
    baseURL = ReadConfig.getApplicationURL()
    #username = ReadConfig.getApplicationUsername()  Not needed for Step 9
    #password =  ReadConfig.getApplicationPassword() Not needed for Step 9
    path = ".//testData/LoginData.xlsx"
    logger=LogGen.loggen()   #Logger variable is created.LogGen.loggen() static method is called

    @pytest.mark.regression               #Based on step 11
    def test_login_ddt(self,setUp):
        self.logger.info("********** Test_002_DDT_Login **********")
        self.logger.info("********** Verifying Login DDT Test **********")
        #self.driver = webdriver.Chrome()
        self.driver = setUp #Whenever we call setUp(fixture) it will return driver
        self.driver.get(self.baseURL)
        #Create object for LoginPage
        self.lp = LoginPage(self.driver)  # __init__(self,driver) is automatically invoked when object lp is created for LoginPage
        # LoginPage constructor is expecting driver as parameter.
        #To access the class variables we have to use self keyword

        self.rows=XLUtils.getRowCount(self.path,'Sheet1')
        print("Number of Rows in a Excel:",self.rows)
        lst_status = [] #Creating empty list to store the status
        for r in range(2,self.rows+1): #Row 1 will be the header.So starting from row 2
            self.user=XLUtils.readData(self.path,'Sheet1',r,1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)      #expected result
            self.lp.setUserName(self.user)      #values are stored in the variables mentioned above
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp=="Pass":
                    self.logger.info("***** Passed *****")
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.exp=="Fail":
                    self.logger.info("***** Failed *****")
                    self.lp.clickLogout()
                    lst_status.append("Fail")
            elif act_title != exp_title:
                if self.exp=="Pass":
                    self.logger.info("***** Failed *****")
                    lst_status.append("Fail")
                elif self.exp=="Fail":
                    self.logger.info("***** Passed *****")
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("**** Login DDT test Passed *****")
            self.driver.close()
            assert True
        else:
            self.logger.info("**** Login DDT test Failed *****")
            self.driver.close()
            assert False
        self.logger.info("***** End of Login DDT Test *****")
        self.logger.info("***** Completed TC_LoginDDT_002 *****")



