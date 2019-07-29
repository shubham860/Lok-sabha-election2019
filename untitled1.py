import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

drivers = webdriver.Chrome("C:\\usr\\chromedriver")

url = "https://en.wikipedia.org/wiki/List_of_United_States_military_bases"

drivers.get(url)
content = driver.page_source
soup = BeautifulSoup(content)

