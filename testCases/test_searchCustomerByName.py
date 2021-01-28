import time

from pageObjects.LoginPage import LoginPage
from pageObjects.addCustomerPage import AddCustomer
from pageObjects.searchCustomerPage import SearchCustomer
from testCases.conftest import tearDown
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_004_SearchCustomerByName:
    baseURL = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_searchCustomerByName(self,setUp):
        self.driver = setUp
        self.driver.get(self.baseURL)
        lp = LoginPage(self.driver)
        lp.setUsername(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()

        self.logger.info("*******************Login Successful**********************")
        self.logger.info("*******************Start searching Customer by Name**********************")

        addcust = AddCustomer(self.driver)
        addcust.clickOnCustomersMenu()  # only these two methods are required from addCustomerPage.py
        addcust.clickOnCustomersMenuItem()

        self.logger.info("*******************Searching Customer by Name**********************")

        searchcust = SearchCustomer(self.driver)
        searchcust.setFirstName("Victoria")
        searchcust.setLastName("Terces")
        searchcust.clickOnSearchButton()
        time.sleep(5)
        status = searchcust.searchCustomerByName("Victoria Terces")
        self.driver.close()
        assert True == status
        self.logger.info("***************Test_004_SearchCustomerByName Finished*********** ")
