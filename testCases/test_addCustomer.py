import random
import string

import pytest

from pageObjects.LoginPage import LoginPage
from pageObjects.addCustomerPage import AddCustomer
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_003_add_customer:
    baseURL = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()


    @pytest.mark.sanity
    @pytest.mark.regression
    def test_add_customer(self,setUp):
        self.logger.info("*********************Login into portal************************")
        self.driver = setUp
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("***********************Login Successful*******************************")
        self.logger.info("***********************Starting addCustomer test*******************************")

        # Creating object of AddCustomer class to access methods
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()
        self.addcust.clickOnAddNewButton()

        self.logger.info("**********************Providing Customer Info******************************")

        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test12345")
        self.addcust.setFirstName("Shilpa")
        self.addcust.setLastName("Chourasia")
        self.addcust.selectGender("Female")
        self.addcust.setDOB("11/12/1989")
        self.addcust.setCompanyName("QAPython")
        #self.addcust.setNewsLetter("Your store name")
        self.addcust.setCustomerRoles("Guests")
        self.addcust.setManagerOfVender("Vendor 1")
        self.addcust.setAdminComments("This is just for testing")
        self.addcust.clickOnSaveButton()

        self.logger.info("**********************Saving Customer Info******************************")
        self.logger.info("**********************Add Customer Validation started******************************")

        self.msg = self.driver.find_element_by_tag_name("body").text
        print(self.msg)

        if "The new customer has been added successfully." in self.msg:
            assert True == True
            self.logger.info("******************test_add_customer test case is passed******************")

        else:
            self.driver.save_screenshots(".\\Screenshots\\" + "test_add_customer.png")
            self.logger.info("********************test_add_customer test case is failed******************")
            assert True == False
        self.driver.close()
        self.logger.info("********************Ending of Test_003_add_customer******************")





def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
