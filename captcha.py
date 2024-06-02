# NOTE: This is currently in progress, this code to skip though captchas is not currently active in the project

import json
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait



#defining anticaptcha function
def acp_api_send_request(driver, message_type, data={}):
    message = {
		# this receiver has to be always set as antiCaptchaPlugin
        'receiver': 'antiCaptchaPlugin',
        # request type, for example setOptions
        'type': message_type,
        # merge with additional data
        **data
    }
    # run JS code in the web page context
    # preceicely we send a standard window.postMessage method
    return driver.execute_script("""
    return window.postMessage({});
    """.format(json.dumps(message)))
# Init the chrome options object for connection the extension

def attempt_a_solve():
    options = webdriver.ChromeOptions()
    # A full path to CRX or ZIP or XPI file which was downloaded earlier 
    options.add_extension('<path to the plugin>')
    # Run the browser (Chrome WebDriver) with passing the full path to the downloaded WebDriver file
    driver = webdriver.Chrome('chromedriver', options=options)

    # Go to the empty page for setting the API key through the plugin API request
    driver.get('https://antcpt.com/blank.html')

    # Setting up the anti-captcha.com API key 
    # replace YOUR-ANTI-CAPTCHA-API-KEY to your actual API key, which you can get from here:
    # https://anti-captcha.com/clients/settings/apisetup
    acp_api_send_request(
        driver,
        'setOptions',
        {'options': {'antiCaptchaApiKey': '<your access token>'}}
    )

    # 3 seconds pause
    time.sleep(3)
    driver.get("URL_HERE")
    # replace the url with the URL you want to scrap

    driver.maximize_window()
    # Test input
    driver.find_element_by_css_selector('span[role=checkbox]').send_keys(Keys.ENTER)

    # Most important part: we wait upto 120 seconds until the AntiCaptcha plugin indicator with antigate_solver class
    # gets the solved class, which means that the captcha was successfully solved
    WebDriverWait(driver, 120).until(lambda x: x.find_element_by_css_selector('.antigate_solver.solved'))

    # Sending form
    driver.find_element_by_css_selector('input[type=submit]').click()

