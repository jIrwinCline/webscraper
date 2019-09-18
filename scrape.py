from bs4 import BeautifulSoup
import requests

with open('index.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

for match in soup.find_all('li', class_='favorites'):
    print(match)

    headline = match.text
    print(headline) 
