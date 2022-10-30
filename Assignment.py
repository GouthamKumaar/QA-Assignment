# 1 importing web driver from selenium
from selenium import webdriver


#2 To overcome "Element Not Interactable Exception Error" which prevents sending keys
#which occurs when internet is slow
#importing time module which helps the browser to load and render the HTML
#also easy to focus on the steps one by one
import time


# 3 from selenium web driver import Select class
#for dropdown field
from selenium.webdriver.support.select import Select


class form_filling():
    def opening_chrome(self):

        # 4 To prevent closing of browser after test completion
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach",True)

        
        # 5 creating object for webdriver
        web = webdriver.Chrome(options=options)

        # 6usinf get method we enter the URL to be opened
        web.get("https://unicreds.com/contact-us")

        # 7 for maximizing the window
        web.maximize_window()

        # 8 attribute sleep is used in time module
        #argument passed here refers the loading time in seconds
        time.sleep(1)

        # 9 storing the name in a variable full_name
        full_name = "Goutham Kumar Reddy"

        # 10 select the DOM element of HTML and interact with them using find_element
        #Copy XPath from DOM element and paste it in find_element
        #first argument is XPath
        #second argument is the XPath which is copied
        name = web.find_element("xpath",'//*[@id="fullname"]')

        # 11 send_keys() used to send particular text to any field which accepts text as input
        #value to be sent here is variable that stoed the name
        name.send_keys(full_name)
        time.sleep(1)

        email_address = "gouthamkumar510@gmail.com"
        email = web.find_element("xpath",'//*[@id="__next"]/div[2]/section/div/div[2]/div[2]/div[2]/div/form/input[2]')
        email.send_keys(email_address)
        time.sleep(1)

        # 12 select the DOM element of HTML and interact with them using find_element
        #Copy XPath from DOM element and paste it in find_element
        #first argument is XPath
        #second argument is the XPath which is copied
        country_code = web.find_element("xpath","//select[@class='p-2 pl-4 pr-4 m-2 mt-2 mb-2 form-control form-control-md']")



        # 13 create a variable and call Select class
        #pass the argument which is the web element on which it is supposed to work
        cc = Select(country_code)



        # 14 selecting by index i.e., 0,1,2,3,4,..... from dropdown field
        cc.select_by_index(3)
        time.sleep(1)

        # 15 selecting by value which is found in the locators
        cc.select_by_value("244")
        time.sleep(1)


        # 16 selecting by visible text which can be seen in dropdown field
        cc.select_by_visible_text("India (+91)")
        time.sleep(1)

        phone = '8500837704'
        ph = web.find_element('xpath','//*[@id="phone"]')
        ph.send_keys(phone)
        time.sleep(1)

        message = ("I'd like to meet with one of your competent education loan counsellors, who will assist me in obtaining a loan with or without collateral")
        msg = web.find_element("xpath",'//*[@id="message"]')
        msg.send_keys(message)
        time.sleep(1)

        submit = web.find_element("xpath",'//*[@id="contactButton"]')

        # 17 click() method used to click particular button
        submit.click()

demo = form_filling()
demo.opening_chrome()

