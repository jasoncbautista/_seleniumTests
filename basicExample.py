from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0


# driver= webdriver.Chrome()


desired_capabilities = webdriver.DesiredCapabilities.IPHONE
desired_capabilities['version'] = '5.0'
desired_capabilities['platform'] = 'MAC'
desired_capabilities['name'] = 'Testing Selenium 2 in Python at Sauce'

driver = webdriver.Remote(
    desired_capabilities=desired_capabilities,
    #command_executor="http://username-string:access-key-string@ondemand.saucelabs.com:80/wd/hub"
    command_executor="http://sqordev:d9c8fd8c-296b-4f71-997b-6a33bc80c483@ondemand.saucelabs.com:80/wd/hub"
)

driver.implicitly_wait(30)

driver= webdriver.remote(
        "ondemand.saucelabs.com"
        , 80
        , "sqordev"
        , "d9c8fd8c-296b-4f71-997b-6a33bc80c483"
);

driver.get('http://sqorweb.local')

try:
    link = driver.find_element_by_css_selector(".dropdown");
    link.click()

    #time.sleep(1)
    links = link.find_elements_by_tag_name("a")
    links[2].click()

    #time.sleep(2)
    driver.get('http://sqorweb.local/team/551/nba/los-angeles-lakers')

    #time.sleep(2)
    links = driver.find_elements_by_tag_name("a")
    #time.sleep(2)
    links[15].click()
    driver.back()
    #time.sleep(4)


    '''
    WebDriverWait(driver, 10).until(EC.title_contains("NBA"))
    teamLink = driver.find_elements_by_css_selector(".team-list-entry")
    teamLink[0].click()
    '''
    #time.sleep(2)


    # Loop
    link = driver.find_element_by_css_selector(".dropdown");
    link.click()
    #time.sleep(2)
    links = link.find_elements_by_tag_name("a")
    links[3].click()
    #time.sleep(2)



    # Loop
    link = driver.find_element_by_css_selector(".dropdown");
    link.click()
    #time.sleep(1)
    links = link.find_elements_by_tag_name("a")
    links[1].click()




    # Loop
    link = driver.find_element_by_css_selector(".dropdown");
    link.click()
    #time.sleep(2)
    links = link.find_elements_by_tag_name("a")
    links[4].click()
    #time.sleep(2)
    driver.back()
    #time.sleep(2)


except (RuntimeError, ValueError, NameError):
    driver.quit()
finally:
    #time.sleep(5)
    driver.quit()

