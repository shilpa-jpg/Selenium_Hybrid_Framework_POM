
# This file is used to read the data from config.ini file
import configparser

config = configparser.RawConfigParser()
config.read(".\\Configuration/config.ini")


class ReadConfig:

    @staticmethod
    def getApplicationUrl():
        url = config.get('Common Data', 'baseURL')
        return url

    @staticmethod
    def getUsername():
        user_name = config.get('Common Data', 'username')
        return user_name

    @staticmethod
    def getPassword():
        pass_word = config.get('Common Data', 'password')
        return pass_word
