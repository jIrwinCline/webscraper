from bs4 import BeautifulSoup
from selenium import webdriver
import requests

s = requests.Session()

s.get("http://dpsstnet.state.or.us/IRIS_PublicInquiry/PrivateSecurity/smsGoPerson.aspx")

r = s.get("http://dpsstnet.state.or.us/IRIS_PublicInquiry/PrivateSecurity/SMSGoPersonLkp.aspx?LkpBy=ID&LkpVal=0").text

soup = BeautifulSoup(r, 'lxml')



for tableInfo in soup.find_all('font'):
    try:
        print(tableInfo.a.text)
    except:
        pass
# officer = tableInfo.td.font.a.text