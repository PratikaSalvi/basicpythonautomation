from  selenium import webdriver
import XLUtils


driver = webdriver.Chrome("C:\chromedrivers\chromedriver.exe")
driver.get("http://newtours.demoaut.com/")
driver.maximize_window()

path = "D:\Book1.xlsx"

rows = XLUtils.getRowCount(path,'Sheet1')

for r in range(2,rows+1):
   username = XLUtils.readData(path,"Sheet1",r,1)
   password = XLUtils.readData(path, "Sheet1", r,2)

   driver.find_element_by_name("userName").send_keys(username)
   driver.find_element_by_name("password").send_keys(password)
   driver.find_element_by_name("login").click()

   if driver.title=="Find a Flight: Mercury Tours:":
      print("Test is passed")
      XLUtils.writeData(path,"Sheet1",r,3,"test passed")
   else:
      print("test not passed")
      XLUtils.writeData(path, "Sheet1", r, 3, "test not passed")


   driver.find_element_by_link_text("home").click()
