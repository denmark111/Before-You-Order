from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Config import *

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")

# Driver for Chrome
driver = webdriver.Chrome(chrome_options=options, executable_path='/usr/lib/chromium-browser/chromedriver')

# Driver for PhantomJS binary
# driver = webdriver.PhantomJS('/root/phantomjs-2.1.1-linux-x86_64/bin/phantomjs')

driver.get(WEB_URL)
driver.quit()

