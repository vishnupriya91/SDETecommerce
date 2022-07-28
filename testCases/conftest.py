#To avoid creating driver object multiple times,we are creating conftest file
from selenium import webdriver
import pytest
'''
@pytest.fixture()
def setUp():
    driver = webdriver.Chrome() #As soon as driver is created ,return the driver
    return driver
'''

#Updating above code based on step 7:
@pytest.fixture()
def setUp(browser): #browser name is given as input in command line in def browser(request) written below
    if browser=='chrome':
        driver = webdriver.Chrome() #As soon as driver is created ,return the driver
        print("Launching Chrome Browser..........")
    elif browser == 'firefox':
        driver = webdriver.Firefox()  # As soon as driver is created ,return the driver
        print("Launching Internet Explorer Browser..........")
    else: #If we forget to pass the browser in command line pytest -v -s testCases/test_login.py --browser chrome it will throw UnboundLocalError.
        driver = webdriver.Chrome() #To avoid UnboundLocalError exception,this else par is written.By default it will launch Chrome browser.
    return driver

def pytest_addoption(parser): #This will get the value from CLI/hooks  ----Its add option dont get confused
    parser.addoption("--browser")

@pytest.fixture()
def browser(request): #This will return browser value to the setup method.
    return request.config.getoption("--browser")  #Command line input

##### Step 8:pytest HTML Report #####

#It is a hook for adding environment info to HTML Reports---These are customizable

def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester Name'] = 'Vishnupriya'

# It is a hook for delete/modify environment info to HTML Reports---These are customizable
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA HOME", None)
    metadata.pop("Plugins", None)







