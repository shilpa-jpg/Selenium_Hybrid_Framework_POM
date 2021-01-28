import time

from pageObjects.LoginPage import LoginPage
from pageObjects.addCustomerPage import AddCustomer
from pageObjects.searchCustomerPage import SearchCustomer
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_004_SearchCustomerByEmail:
    baseURL = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_searchCustomerByEmail(self,setUp):
        self.driver = setUp
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.logger.info("*******************Login Successful**********************")
        self.logger.info("*******************Start searching Customer by Email**********************")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()   # only these two methods are required from addCustomerPage.py
        self.addcust.clickOnCustomersMenuItem()

        self.logger.info("*******************Searching Customer by Email**********************")

        # creating object of SearchCustomer class to access methods
        searchcust = SearchCustomer(self.driver)
        searchcust.setEmail("victoria_victoria@nopCommerce.com")
        searchcust.clickOnSearchButton()
        time.sleep(5)
        status = searchcust.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        self.driver.close()
        assert True==status
        self.logger.info("***************Test_004_SearchCustomerByEmail Finished*********** ")







