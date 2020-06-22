
#First basic coding for selenium with python

from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome("C:\chromedrivers\chromedriver.exe")
# to open website on Chrome Browser write website name
driver.get("xxxxxxxxxxxxx")

time.sleep(1000)
#Enter Username
driver.find_element_by_name("userName").send_keys("xxxxxxxxx")
#Enter Password
driver.find_element_by_name("password").send_keys("xxxxxxxxxx")
#Click on Login  button
driver.find_element_by_name("login").click()
driver.implicitly_wait(30)

#Select the  Dropdown for No of Passenger
element = driver.find_element_by_name("passCount")
numbedrop = Select(element)
#Select count 3
numbedrop.select_by_value("3")

#Select dropdown for portname
element1 = driver.find_element_by_name("fromPort")
departure = Select(element1)
departure.select_by_index(3)

#Select the  dropdown for month
element2 = driver.find_element_by_name("fromMonth")
Month = Select(element2)
Month.select_by_visible_text("April")

#Select the  date of depature
element2 = driver.find_element_by_name("fromDay")
Month = Select(element2)
Month.select_by_visible_text("2")

