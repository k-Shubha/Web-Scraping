# Web-Scraping
### What is web-scraping?
Web scraping, web harvesting, or web data extraction is data scraping used for extracting data from websites.

Web scraping helps us extract large volumes of data about customers, products, people, stock markets, etc. 
It is usually difficult to get this kind of information on a large scale using traditional data collection methods. 
We can utilize the data collected from a website such as e-commerce portal, social media channels to understand customer behaviors and sentiments, buying patterns, and brand attribute associations which are critical insights for any business.

### Installation
#### $ pip install selenium
Selenium python API requires a web driver to interface with your choosen browser. The corresponding web drivers can be downloaded from the following links. And also make sure it is in your PATH, e.g. /usr/bin or /usr/local/bin. For more information regarding installation, please refer to the [link.](https://selenium-python.readthedocs.io/installation.html)

The first and foremost thing while scraping a website is to understand the structure of the website.

### Importing packages
from selenium import webdriver
### create a new instance of google chrome. This will help program open an url in google chrome.
driver = webdriver.Chrome('Path in your computer where you have installed chromedriver')

### Let’s now access google chrome and open website.
driver.get('url')
