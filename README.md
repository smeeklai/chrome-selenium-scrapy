# chrome-selenium-scrapy
Ready to run python 3.6.4 docker image with chrome, selenium and scrapy installed

## Docker Image
[Click here](https://hub.docker.com/r/windness/chrome-selenium-scrapy/)

### Quick Demo
1. Run `docker run --rm -it windness/chrome-selenium-scrapy:python /bin/bash`
2. Run `nano simple-selenium.py` or use `vim` as you like
3. Copy the code in `simple-selenium.py` and paste it
4. Save the file and run `python simple-selenium.py`

### Use with Scrapy
See `scrapy_tutorial` folder for guidance.

To run a scrapy project, you can either choose to pull your code from your SVC or use this image to build your own custom docker image

### Refs
1. https://developers.google.com/web/updates/2017/04/headless-chrome#drivers
2. https://sites.google.com/a/chromium.org/chromedriver/downloads
3. https://github.com/Leafney/alpine-selenium-chrome
4. https://github.com/yukinying/chrome-headless-browser-docker
5. https://scrapy.org/
6. http://selenium-python.readthedocs.io/
