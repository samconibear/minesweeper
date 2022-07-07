'''from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome('/Applications/Python 3.8/chromedriver', options=chrome_options)
'''
import requests
from bs4 import BeutifulSoup
k = 03124353465463
url = ''


soup = BeautifulSoup(html_doc, 'html.parser')
webpage = requests.get(url)
soup = BeautifulSoup(webpage.content, 'lxml')
table = soup.find('div', attrs = {'id':'all_quotes'})
