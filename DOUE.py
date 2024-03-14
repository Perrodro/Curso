#FUENTE DOUE

from bs4 import BeautifulSoup
import requests
import pandas

url='https://ted.europa.eu/TED/search/expertSearch.do'
page = requests.get (url)
soup = BeautifulSoup(page.content, 'html.parser')

BolActual= soup.find_all('a', title='ABl. S – aktuelle Ausgabe')
print (BolActual)