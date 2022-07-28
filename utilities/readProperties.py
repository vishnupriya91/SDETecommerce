import configparser  #it is a package in python

config=configparser.RawConfigParser()  #Object is created for RawConfigParser() Class
config.read(".\\configurations\\config.ini")

class ReadConfig():
    @staticmethod   #Methods can be accessed directly by class name without creating any objects
    def getApplicationURL():
        url=config.get('common Info','baseURL')
        return url

    @staticmethod  # Methods can be accessed directly by class name without creating any objects
    def getApplicationUsername():
        username = config.get('common Info', 'username')
        return  username

    @staticmethod  # Methods can be accessed directly by class name without creating any objects
    def getApplicationPassword():
        password = config.get('common Info', 'password')
        return password