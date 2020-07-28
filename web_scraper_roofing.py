import bs4
from bs4 import BeautifulSoup
import requests
from re import search

soup_city_link = []
soup_roofer_link = []
name=''
address=''
service=''

output = []
output.append("Name"+"|"+"Address"+"|"+"Service")

response_city = requests.get("https://hipages.com.au/find/roofing/qld",allow_redirects=False)
soup = BeautifulSoup(response_city.content,"html.parser")
soup_city = soup.findAll("li",{"class":"sc-chPdSV hHYFnl"})

for x in range(len(soup_city)):
    soup_city_link.append(soup_city[x].a['href'])
    response_roofer = requests.get("https://hipages.com.au"+soup_city[x].a['href'],allow_redirects=False)
    soup = BeautifulSoup(response_roofer.content,"html.parser")
    soup_roofer = soup.findAll("div",{"class":"thumbnail__ThumbnailContainer-ika75i-0 eAKlft"})
    for y in range(len(soup_roofer)):
        soup_roofer_link.append(soup_roofer[y].a['href'])
        response_final = requests.get("https://hipages.com.au"+soup_roofer[y].a['href'],allow_redirects=False)
        soup = BeautifulSoup(response_final.content,"html.parser")
        final_response_without_phone = soup.findAll("span",{"class":"Contact__Item-sc-1giw2l4-2 kBpGee"})
        #website_parse = soup.findAll("a",{"class":"sc-AykKC col__Col-sc-15n4ng3-0 hJfjKg"})
        #website_parse = soup.findAll("a",{"class":"sc-AykKC col__Col-sc-15n4ng3-0 hJfjKg"})
        #print(website_parse)
        
        for z in range(len(final_response_without_phone)):
            image_src = final_response_without_phone[z].img['src']
            if search('contact', image_src):
                name = final_response_without_phone[z].text.strip()
            elif search('loc', image_src):
                address = final_response_without_phone[z].text.strip()
            elif search('servicing', image_src):
                service = final_response_without_phone[z].text.strip()
            elif search('phone', image_src):
                phone = final_response_without_phone[z].text.strip()
            elif search('mobile', image_src):
                mobile = final_response_without_phone[z].text.strip()
            elif search('fax', image_src):
                fax = final_response_without_phone[z].text.strip()
        output.append(name+"|"+address+"|"+service)
        name=''
        address=''
        service=''


with open('output.txt', 'w') as filehandle:
    for listitem in output:
        filehandle.write('%s\n' % listitem)