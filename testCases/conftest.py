from selenium import webdriver
import pytest


@pytest.fixture()
def setUp(browser):
    if (browser == "chrome"):
        driver = webdriver.Chrome(
            "C:\\Users\\shilp\\Downloads\\UFT_One_15.0_DVD\\Unified Functional Testing\\MSI\\Micro Focus\\Unified Functional Testing\\bin\\WebDriver\\chromedriver.exe")
        print("Launching Chrome browser")
    else:
        browser == "firefox"
        driver = webdriver.Firefox("C:\\Users\\shilp\\AppData\\Local\\Mozilla Firefox\\firefox.exe")
        print("Launching Firefox browser")
    driver.maximize_window()
    return driver


@pytest.fixture()
def tearDown():
    driver = webdriver.Chrome
    driver.close()


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


######Code to generate the HTML reports
# This hook is for adding env info to HTML report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester Name'] = 'Shilpa'


# This hook for deleting/modifying env info to HTML report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA HOME", None)
    metadata.pop("Plugins", None)
