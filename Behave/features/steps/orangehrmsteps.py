
from  behave import *
from selenium import  webdriver

@given(u'launch chromebrowser')
def launch_chromedriver(context):
    context.driver=webdriver.Chrome(executable_path ="C:\chromedrivers\chromedriver.exe")


@when(u'open orange HRM homepage')
def open_Homepage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@then(u'veriy logo is present on main page')
def verify_logo(context):
    status = context.driver.find_element_by_xpath("//div[@id='divLogo']//img").is_displayed()
    assert status is True

@then(u'Close browser')
def close_browser(context):
    context.driver.close()

