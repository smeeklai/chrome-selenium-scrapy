from selenium import webdriver

# Initiate driver
options = webdriver.ChromeOptions()
options.binary_location = '/usr/bin/google-chrome-unstable'
options.add_argument('headless')
options.add_argument('no-sandbox')
options.add_argument('disable-gpu')
options.add_argument('disable-dev-shm-usage')
options.add_argument('window-size=1200x600')
driver = webdriver.Chrome(chrome_options=options)

# Example
driver.get('https://scrapy.org/')
title = driver.title
print(title.encode('utf-8'))

# Release memory
driver.close()
driver.quit()