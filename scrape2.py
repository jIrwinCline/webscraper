from bs4 import BeautifulSoup
from selenium import webdriver
import requests
chrome_path = r"C:\Users\jakob\Desktop\chromedriver.exe"

driver = webdriver.Chrome(chrome_path)
#NAV TO PAGE W/ SESSION
r = driver.get("http://dpsstnet.state.or.us/IRIS_PublicInquiry/PrivateSecurity/SMSGoPersonLkp.aspx")
driver.get("http://dpsstnet.state.or.us/IRIS_PublicInquiry/PrivateSecurity/SMSGoPersonLkp.aspx?LkpBy=ID&LkpVal=0")

#CLICK NAME

driver.find_element_by_xpath("""//*[@id="DataGridAgcyEmp"]/tbody/tr[2]/td[1]/font/a""").click()

# find info
infos = driver.find_elements_by_tag_name("font")

for infos in infos:
    try:
        print(infos.text)
    except:
        pass

# GO BACK

# driver.execute_script("window.history.go(-1)")

# r.find_element_by_xpath("""//*[@id="DataGridAgcyEmp"]/tbody/tr[52]/td/font/b/a""").click()

# for tableInfo in soup.find_all('font'):
#     try:
#         print(tableInfo.a.text)
#     except:
#         pass