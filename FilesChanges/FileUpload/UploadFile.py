from selenium import webdriver

driver = webdriver.Chrome("C:\chromedrivers\chromedriver.exe")

#Maximize the window
driver.maximize_window()
#Open the Url in Browser
driver.get("http://testautomationpractice.blogspot.com/")

#1st approch specify pixel
#driver.execute_script("window.scrollBy(0,1000)","")

#2nd approch by finding the element
driver.implicitly_wait(30)
flag = driver.find_element_by_id("FSsubmit")
driver.execute_script("arguments[0].scrollIntoView():",flag)

#3rd Scrool to the end of the page
#driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")