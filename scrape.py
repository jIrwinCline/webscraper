from bs4 import BeautifulSoup
import requests

s = requests.Session()

s.get("http://dpsstnet.state.or.us/IRIS_PublicInquiry/PrivateSecurity/smsGoPerson.aspx")

r = s.get("http://dpsstnet.state.or.us/IRIS_PublicInquiry/PrivateSecurity/SMSGoPersonLkp.aspx?LkpBy=ID&LkpVal=0").text

soup = BeautifulSoup(r, 'lxml')



for tableInfo in soup.find_all('font'):
    if tableInfo.find_all('a'):
        print(tableInfo.a.text)
# officer = tableInfo.td.font.a.text