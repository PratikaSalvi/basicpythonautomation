from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome("C:\chromedrivers\chromedriver.exe")

#Maximize the window
driver.maximize_window()
#Open the Url in Browser
driver.get("http://demo.automationtesting.in/Windows.html")
#Click on button Click
driver.find_element_by_link_text("click").click()
#parent window handle
handleValue= driver.current_window_handle
#print parent handle value
print("This is value "+handleValue)
for handle in driver.window_handles:

    if handle != handleValue:

        print(handle)
        driver.switch_to.window(handle)

#Hover on Documentation
documentation =driver.find_element_by_link_text("Documentation")
#Create object for Action
actions= ActionChains(driver)
actions.move_to_element(documentation)
actions.perform()

driver.implicitly_wait(20)

#Click on options Web
driver.find_element_by_link_text("Web").click()
driver.switch_to.window(handleValue)


driver.quit()