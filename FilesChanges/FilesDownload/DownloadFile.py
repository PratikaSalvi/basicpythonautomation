from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#Create an object name chromeOptions
chromeOptions = Options()
#add a variable name Downloaddefaultpath and location to save the file
chromeOptions.add_experimental_option("prefs",{"Downloaddefaultpath":"D:\Downloads"})
driver = webdriver.Chrome("C:\chromedrivers\chromedriver.exe",options=chromeOptions)

#Maximize the window
driver.maximize_window()
#Open the Url in Browser
driver.get("http://demo.automationtesting.in/FileDownload.html")
#Enter the  text to enable the Generate button
driver.find_element_by_id("textbox").send_keys("Hello")
#Click on Generate Button
driver.find_element_by_id("createTxt").click()
#Click on Download Button
driver.find_element_by_link_text("Download").click()
#Save the screenshot
driver.save_screenshot("D:\Downloads\Image1.png")
#close the browser
driver.close()
