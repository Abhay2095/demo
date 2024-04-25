import pytest
import configparser

config = configparser.RawConfigParser()

config.read("E:\\nopcommerce\\Configurations\\Config.ini")

class Readconfig:
    @staticmethod
    def getbaseurl():
        baseurl = config.get('base info', 'baseurl')
        return baseurl

    @staticmethod
    def getemail():
        email = config.get('base info', 'email')
        return email

    @staticmethod
    def getpassword():
        password = config.get('base info', 'password')
        return password
























