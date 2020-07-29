import bs4
from bs4 import BeautifulSoup
import requests
from re import search

company_name_list = []
company_name=''
website=''

delimiter="|"
output = []
output.append("Company_name"+delimiter+"Website")

response_company = requests.get("https://www.producthunt.com/newest",allow_redirects=False)
soup = BeautifulSoup(response_company.content,"html.parser")
soup_company = soup.findAll("div",{"class":"item_54fdd"})
#print(soup_company[0].a['href'])

for x in range(len(soup_company)):
    company_name = soup_company[x].h3.text.strip()
    response_roofer = requests.get("https://www.producthunt.com"+soup_company[x].a['href'],allow_redirects=False)
    soup = BeautifulSoup(response_roofer.content,"html.parser")
    soup_website = soup.find("div",{"class":"side_c0705"})
    #print(soup_website)
    if soup_website != None:
        website = soup_website.span['title']
        print(company_name+delimiter+website)
        company_name=''
        website=''

# with open('output.txt', 'w') as filehandle:
#     for listitem in output:
#         filehandle.write('%s\n' % listitem)