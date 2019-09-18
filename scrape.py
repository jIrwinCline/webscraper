from bs4 import BeautifulSoup
import requests

s = requests.Session()

s.get("http://dpsstnet.state.or.us/IRIS_PublicInquiry/PrivateSecurity/smsGoPerson.aspx")

r = s.get("http://dpsstnet.state.or.us/IRIS_PublicInquiry/PrivateSecurity/SMSGoPersonLkp.aspx?LkpBy=ID&LkpVal=0").text

soup = BeautifulSoup(r, 'lxml')



tableInfo = soup.find('tr')

print(tableInfo.prettify())


# soup = BeautifulSoup(source, 'lxml')