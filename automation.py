from selenium import webdriver #allow us to drive the web through code
#driver : each browser has different drivers

chrome_browser = webdriver.Chrome('./chromedriver') # initiate the driver to run Chrome
print(chrome_browser)

chrome_browser.maximize_window() # to maximize chrome browser
chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html') # this get chrome to go to specific url
# == $0 type $0 inside the website console, it will show the element that we have captured
assert 'Selenium Easy Demo' in chrome_browser.title # assert is a good way to test if something is exist or not, if it is False, it exit the code immediately and error out
show_message_button = chrome_browser.find_element_by_class_name('btn-default') # Grab the button from the website
print(show_message_button.get_attribute('innerHTML')) # grab everything inside the code, the text inside, and then print out the text

assert 'Show Message' in chrome_browser.page_source

user_message= chrome_browser.find_element_by_id('user-message') # grab the id text from the website
#user_button2 = chrome_browser.find_element_by_css_selector('#get-input > .btn') # same as above goal, # stands for id, get-input is a form above button mean grab everything that is child of button
user_message.clear()
user_message.send_keys('Anh yeu CiCi nhieu nhat') # Mimic what we input into the 'input message' on the website

show_message_button.click() # click the button that we grab from the browser

output_message = chrome_browser.find_element_by_id('display') # grab the element by id name :'display', to actually grab the output message

assert 'Anh yeu CiCi nhieu nhat' in output_message.text # to test if the code grab the elements we need

# chrome_browser.close() # close our browser, only once
#chrome_browser.quit() # quit mean close the entire chrome driver and all other

# With automation you can create bot to upvote something, or like comment to increase popularity ( this is bad affection)
# Solution is that verify you are a HUMAN

# With automation you can benefit testing skills