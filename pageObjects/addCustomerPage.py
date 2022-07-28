import  time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

class AddCustomer:
    #Add Customer Page
    lnkCustomers_menu_xpath ="//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustomers_menuitem_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btnAddnew_xpath = "//a[@class='btn btn-primary']"
    txtemail_xpath = "//input[@id='Email']"
    txtpassword_xpath = "//input[@id='Password']"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    rdMaleGender_id = "Gender_Male"
    rdFemaleGender_id = "Gender_Female"
    txtDOB_xpath = "//input[@id='DateOfBirth']"
    txtCompanyName_xpath ="//input[@id='Company']"
    txtCustomerRoles_xpath = '//*[@id="customer-info"]/div[2]/div[10]/div[2]/div/div[1]/div/div'
    lstitemAdministrators_xpath = "//li[contains(text(),'Administrators')]"
    lstitemRegistered_xpath = "//li[contains(text(),'Registered')]"
    lstitemGuest_xpath = "//li[contains(text(),'Guests')]"
    lstitemsVendors_xpath = "//li[contains(text(),'Vendors')]"
    #drpmgrOfVendor_xpath = "//select[@id='VendorId']"
    txtAdminComment_xpath = "//textarea[@id='AdminComment']"
    btnSave_xpath = "//button[@name='save']"

    def __init__(self,driver):
        self.driver = driver

    def clickOnCustomersMenu(self):
        self.driver.find_element(By.XPATH,self.lnkCustomers_menu_xpath).click()

    def clickOnCustomersMenuItem(self):
        self.driver.find_element(By.XPATH,self.lnkCustomers_menuitem_xpath).click()

    def clickOnAddNew(self):
        self.driver.find_element(By.XPATH,self.btnAddnew_xpath).click()

    def setEmail(self,email):
        self.driver.find_element(By.XPATH,self.txtemail_xpath).send_keys(email)

    def setPassword(self, password):
            self.driver.find_element(By.XPATH, self.txtpassword_xpath).send_keys(password)

    def setFirstName(self,fname):
        self.driver.find_element(By.XPATH,self.txtFirstName_xpath).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element(By.XPATH,self.txtLastName_xpath).send_keys(lname)

    def setGender(self, gender):
        if gender == 'Male':
            self.driver.find_element(By.ID, self.rdMaleGender_id).click()
        elif gender == 'Female':
            self.driver.find_element(By.ID, self.rdFemaleGender_id).click()
        else:
            self.driver.find_element(By.ID, self.rdMaleGender_id).click()  # Default

    def setDob(self, dob):
        self.driver.find_element(By.XPATH, self.txtDOB_xpath).send_keys(dob)

    def setCompany(self,comname):
        self.driver.find_element(By.XPATH,self.txtCompanyName_xpath).send_keys(comname)

    def setCustomerRoles(self,role):
        self.driver.find_element(By.XPATH,self.txtCustomerRoles_xpath).click()
        time.sleep(3)
        if role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH,self.lstitemRegistered_xpath)
        elif role == 'Administrators':
            self.listitem = self.driver.find_element(By.XPATH,self.lstitemAdministrators_xpath)
        elif role == 'Guests':
            #Here the user can be either Registered (or) Guest
            time.sleep(3)
            self.driver.find_element(By.XPATH,"//span[2][@class='k-select']").click()
            self.listitem = self.driver.find_element(By.XPATH,self.lstitemGuest_xpath)
        elif role == 'Vendors':
            self.listitem = self.driver.find_element(By.XPATH,self.lstitemsVendors_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemGuest_xpath)   #Dehault
        time.sleep(3)
        #self.listitem.click();         #Sometimes this statement will not work.so use execute_script (Javascript Statement)
        self.driver.execute_script("arguments[0].click();",self.listitem)

    #def setManagerOfVendor(self,value):
        #drp = self.driver.find_element(By.XPATH,self.drpmgrOfVendor_xpath)
        #drp.select_by_visible_text(value)

    def setAdminComment(self,comment):
        self.driver.find_element(By.XPATH,self.txtAdminComment_xpath).send_keys(comment)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH,self.btnSave_xpath).click()









