import time

from selenium.webdriver.support.select import Select


class AddCustomer:
    #Locators
    link_customer_menu_xpath = '//a[@href="#"]//span[contains(text(),"Customers")]'
    link_customer_menuitem_xpath = '//a[@href="/Admin/Customer/List"]//span[contains(text(),"Customers")]'
    btnAddnew_xpath = '//a[@class="btn bg-blue"]'
    txt_email_xpath = '//input[@id = "Email"]'
    txt_password_xpath = '//input[@id = "Password"]'
    txtFirst_name_id = 'FirstName'
    txtLast_name_id = 'LastName'
    rdMaleGender_id = 'Gender_Male'
    rdFemaleGender_id = 'Gender_Female'
    txtDOB_xpath = '//input[@id = "DateOfBirth"]'
    txtCompanyName_xpath = '//input[@id = "Company"]'
    txtNewsletter_xpath = '//select[@id="SelectedNewsletterSubscriptionStoreIds"]'
    txt_customerRoles_xpath = '//div[@class="k-multiselect-wrap k-floatwrap"]'
    lstitemRegistered_xpath = '//li[contains(text(),"Registered")]'
    lstitemAdministrators_xpath = '//li[contains(text(),"Administrators")]'
    lstitemGuests_xpath = '//li[contains(text(),"Guests")]'
    lstitemVendors_xpath = '//li[contains(text(),"Vendors")]'
    drp_vendor_xpath = '//select[@id = "VendorId"]'
    txtAdminContent_xpath = "//textarea[@id='AdminComment']"
    btnSave_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomersMenu(self):
        self.driver.find_element_by_xpath(self.link_customer_menu_xpath).click()

    def clickOnCustomersMenuItem(self):
        self.driver.find_element_by_xpath(self.link_customer_menuitem_xpath).click()

    def clickOnAddNewButton(self):
        self.driver.find_element_by_xpath(self.btnAddnew_xpath).click()

    def setEmail(self, email):
        self.driver.find_element_by_xpath(self.txt_email_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element_by_xpath(self.txt_password_xpath).send_keys(password)

    def setFirstName(self, fname):
        self.driver.find_element_by_id(self.txtFirst_name_id).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element_by_id(self.txtLast_name_id).send_keys(lname)

    def selectGender(self, gender):
        if gender == "Female":
            self.driver.find_element_by_id(self.rdFemaleGender_id).click()
        elif gender == "Male":
            self.driver.find_element_by_id(self.rdMaleGender_id).click()

    def setDOB(self, dob):
        self.driver.find_element_by_xpath(self.txtDOB_xpath).send_keys(dob)

    def setCompanyName(self, companyname):
        self.driver.find_element_by_xpath(self.txtCompanyName_xpath).send_keys(companyname)

    def setNewsLetter(self,value):
        drp = Select(self.driver.find_element_by_xpath(self.txtNewsletter_xpath))
        drp.select_by_visible_text(value)


    def setCustomerRoles(self, role):
        self.driver.find_element_by_xpath(self.txt_customerRoles_xpath).click()
        time.sleep(5)
        if role == "Registered":
            self.lstitem = self.driver.find_element_by_xpath(self.lstitemRegistered_xpath)

        elif role == "Administrators":
            self.lstitem = self.driver.find_element_by_xpath(self.lstitemAdministrators_xpath)

        elif role == "Guests":
            time.sleep(3)
            self.driver.find_element_by_xpath("//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.lstitem = self.driver.find_element_by_xpath(self.lstitemGuests_xpath)

        elif role == "Registered":
            self.lstitem = self.driver.find_element_by_xpath(self.lstitemRegistered_xpath)

        elif role == "Vendors":
            self.lstitem = self.driver.find_element_by_xpath(self.lstitemVendors_xpath)

        else:
            self.lstitem = self.driver.find_element_by_xpath(self.lstitemGuests_xpath)
        time.sleep(3)

        self.driver.execute_script("arguments[0].click();", self.lstitem)

    def setManagerOfVender(self, value):
        drp = Select(self.driver.find_element_by_xpath(self.drp_vendor_xpath))
        drp.select_by_visible_text(value)

    def setAdminComments(self,txt):
        self.driver.find_element_by_xpath(self.txtAdminContent_xpath).send_keys(txt)

    def clickOnSaveButton(self):
        self.driver.find_element_by_xpath(self.btnSave_xpath).click()
