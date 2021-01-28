import pytest

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    # Creating object of Loggen class to access Loggen class methods
    logger = LogGen.loggen()

    @pytest.mark.sanity
    # Test case to verify homepage title
    def test_homePageTitle(self, setUp):
        # setUp is fixture which is created in conftest.py file
        self.logger.info("*************************Test_001_Login******************")
        self.logger.info("*************************Verifying Home Page title******************")
        self.driver = setUp
        # setUp method is returning driver which we are storing in self.driver
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("*************************test_homePageTitle is passed******************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.error("*************************test_homePageTitle is Failed******************")
            assert False

    @pytest.mark.sanity
    # Login Method
    def testLogin(self, setUp):
        self.logger.info("****************Verifying testLogin*****************")
        self.driver = setUp
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.save_screenshot(".\\Screenshots\\" + "testLogin.png")
            self.driver.close()
            self.logger.info("****************testLogin is passed*****************")
        else:
            self.driver.close()
            self.logger.error("****************testLogin is failed*****************")
            assert False





