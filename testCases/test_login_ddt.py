import time

import pytest

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils


# Command to run this prog : pytest -s -v testCases/test_login_ddt.py --html=Reports\report.html --browser=chrome

class Test_002_Login_DDT:
    baseURL = ReadConfig.getApplicationUrl()
    path = ".//TestData/LoginData.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def testLogin_ddt(self, setUp):
        self.logger.info("****************Test_002_Login_DDT*****************")
        self.logger.info("****************Verifying testLogin_ddt*****************")
        self.driver = setUp
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)

        # To read no. of rows from excel
        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print("No. of rows in excel:", self.rows)

        Empty_list = []
        for r in range(2, self.rows + 1):
            self.excel_username = XLUtils.readData(self.path, 'Sheet1', r,
                                                   1)  # 1 represent column 1 that is username in excel
            self.excel_password = XLUtils.readData(self.path, 'Sheet1', r,
                                                   2)  # It will read password column and will return passwords
            self.Expected_Result = XLUtils.readData(self.path, 'Sheet1', r,
                                                    3)  # It represent 3 column in excel that is status column

        # Call setUsername method from LoginPage.py and pass username and password from excel
        self.lp.setUsername(self.excel_username)
        self.lp.setPassword(self.excel_password)
        self.lp.clickLogin()
        time.sleep(5)

        act_title = self.driver.title
        exp_title = "Dashboard / nopCommerce administration"
        if act_title == exp_title:
            if self.Expected_Result == "Pass":
                self.logger.info("******************Test is passed for ddt**********************")
                self.lp.clickLogout()
                Empty_list.append("Pass")

            elif self.Expected_Result == "Fail":
                self.logger.info("************************Test is Failed for ddt**************************")
                self.lp.clickLogout()
                Empty_list.append("Fail")

        elif act_title != exp_title:
            if self.Expected_Result == "Pass":
                self.logger.info('**********************est is Failed for ddt****************************')
                Empty_list.append("Fail")

            elif self.Expected_Result == "Fail":
                self.logger.info('***************************Test is passed for ddt******************************')
                Empty_list.append('Pass')

        if "Fail" not in Empty_list:
            self.logger.info("********************Test_002_Login_DDT is passed**********************")
            self.driver.close()
            assert True
        else:
            self.logger.info("********************Test_002_Login_DDT is failed**********************")
            self.driver.close()
            assert False
