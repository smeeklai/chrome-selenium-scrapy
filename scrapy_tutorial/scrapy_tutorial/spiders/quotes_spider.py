import scrapy
from selenium import webdriver

class QuotesSpider(scrapy.Spider):
    """
    A sample class that shows you how to use selenium web driver with scrapy
    """
    name = "quotes"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print ("Start Driver ...")
        options = webdriver.ChromeOptions()
        options.binary_location = '/usr/bin/google-chrome-unstable'
        options.add_argument('headless')
        options.add_argument('no-sandbox')
        options.add_argument('disable-gpu')
        options.add_argument('disable-dev-shm-usage')
        options.add_argument('window-size=1200x600')
        self.driver = webdriver.Chrome(chrome_options=options)

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        self._get_page(response.url)
        # Do something...
        self._close_driver()

    def _close_driver(self):
        print ("Closing Driver ...")
        self.driver.close()
        self.driver.quit()

    def _get_page(self, url):
        print ("Getting Page ...")
        self.driver.get(url)
