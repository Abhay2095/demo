import pytest
import configparser

config = configparser.RawConfigParser()

config.read("E:\\nopcommerce12\\Configurations\\Config.ini")

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

    @staticmethod
    def getPassword():
        Password = config.get('add info', 'Password')
        return Password

    @staticmethod
    def getfname():
        fname = config.get('add info', 'fname')
        return fname

    @staticmethod
    def getlname():
        lname = config.get('add info', 'lname')
        return lname

    @staticmethod
    def getDOB():
        DOB = config.get('add info', 'DOB')
        return DOB

    @staticmethod
    def getcname():
        cname = config.get('add info', 'cname')
        return cname

    @staticmethod
    def getcontent():
        content = config.get('add info', 'content')
        return content




















