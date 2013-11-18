import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0


driver= webdriver.Chrome()
driver.get('http://sqorweb.local')

try:
    link = driver.find_element_by_css_selector(".dropdown");
    link.click()

    links = link.find_elements_by_tag_name("a")
    links[2].click()

    WebDriverWait(driver, 10).until(EC.title_contains("NBA"))
    teamLink = driver.find_elements_by_css_selector(".team-list-entry")
    teamLink[0].click()


except (RuntimeError, ValueError, NameError):
    driver.quit()
finally:
    time.sleep(5)
    driver.quit()

