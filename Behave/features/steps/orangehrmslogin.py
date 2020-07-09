from behave import *
from selenium import webdriver

@given('Browser used should be Chrome Browser')
def launch_chromebrowser(context):
    context.driver = webdriver.Chrome(executable_path="C:\chromedrivers\chromedriver.exe")


@when('I open HRMS Homepage')
def open_Homepage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")

@when('Enter username "{user}" and password "{pwd}"')
def enter_credential(context, user, pwd):
    context.driver.find_element_by_id("txtUsername").send_keys(user)
    context.driver.find_element_by_id("txtPassword").send_keys(pwd)

@when('Click on Login Button')
def login_click(context):
    context.driver.find_element_by_id("btnLogin").click()


@then('User should get Logged In and land on Dashboard')
def step_impl(context):
    try:
        text = context.driver.find_element_by_xpath("//h1[contains(text(),'Dashboard')]").text
    except:
        context.driver.close()
        assert False, "Test Failed"
    if text == "Dashboard":
        context.driver.close()
        assert True, "Test Passed"



