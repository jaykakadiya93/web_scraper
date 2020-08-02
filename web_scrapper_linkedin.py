from selenium import webdriver
import bs4
from bs4 import BeautifulSoup
delimiter="|"
output = []
Company_name=''
Employee_name=''
Employee_position=''
Linkein_url=''
output.append("Company_name"+delimiter+"Employee_name"+delimiter+"Employee_position"\
    +delimiter+"Linkein_url")

url = "https://www.linkedin.com/uas/login/"

driver = webdriver.Chrome()
driver.get(url)

elementID = driver.find_element_by_id('username')
elementID.send_keys('linkedin email address')

elementID = driver.find_element_by_id('password')
elementID.send_keys('password')

elementID.submit()

driver.get('https://www.linkedin.com/search/results/people/?facetCurrentCompany=%5B%2261712%22%5D')

source_code = BeautifulSoup(driver.page_source,features="lxml")
soup = source_code.findAll("div",{"class":"search-result__info pt3 pb4 ph0"})
#soup_employee_name = source_code.findAll("span",{"class":"name actor-name"})
#soup_linkedin_url = source_code.findAll("a",{"class":"search-result__result-link ember-view"})
#soup_company = source_code.findAll("p",{"class":"subline-level-1 t-14 t-black t-normal search-result__truncate"})
for x in range(len(soup)):
    soup_employee = soup[x].find("span",{"class":"name actor-name"})
    if soup_employee != None:
        #Employee_name = soup_employee.span.text.strip()
        Linkein_url = soup[x].a['href']
        company = soup[x].p.text.strip()
        print(Employee_name+delimiter+Linkein_url+delimiter+company)
        Employee_name=''
        Linkein_url=''
        company=''
        soup_employee=''
