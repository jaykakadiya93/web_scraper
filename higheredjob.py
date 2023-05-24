import requests
from bs4 import BeautifulSoup
import json
import time

from typing import List

API_KEY = ''
start_row = -1
NUM_JOBS = 100
async_link=[]
def get_job_batch(start_row: int) -> List[str]:
    list_virw_skeleton_url = f'https://www.higheredjobs.com/adjunct/search.cfm?PosType=2&type=1&StartRow={start_row}&SortBy=4&NumJobs={NUM_JOBS}'
    print(list_virw_skeleton_url)
    payload = {'api_key': API_KEY, 'url': list_virw_skeleton_url}
    res = requests.get('http://api.scraperapi.com', params=payload)
    soup = BeautifulSoup(res.text,features="html.parser")
    records = soup.find_all('div', {'class': 'record'})
    job_detail_links = []
    for record in records:
        job_title_href = f'https://www.higheredjobs.com/adjunct/{record.find("a")["href"]}'
        job_detail_links.append(job_title_href)
    return job_detail_links


jobs_batch = get_job_batch(start_row=start_row)


#jobs_batch = ['https://www.higheredjobs.com/adjunct/details.cfm?JobCode=178371614&Title=Exam%20Question%20Category%20Taggers%20%28Contract%29']

def scrape_higheredjobs_detail_page(link: str):
    payload = {'apiKey': API_KEY, 'url': link}
    res = requests.post('https://async.scraperapi.com/jobs', json=payload)
    y = json.loads(res.text)
    # time.sleep(5)
    async_link.append(y["statusUrl"])
    print(y["statusUrl"])

def scrape_jobs(url: str):

    resq = requests.get(url = url)
    y1 = json.loads(resq.text)

    soup = BeautifulSoup(y1["response"]["body"],features="html.parser")

    job_title = soup.find('h1', {'id': 'jobtitle-header'}).get_text(strip=True)
    institution = soup.find('div', {'class': 'job-inst'}).get_text(strip=True)
    location = soup.find('div', {'class': 'job-loc'}).get_text(strip=True)
    if location[:3] == 'in\n':
        location = location[5:].strip()

    job_info_raw = soup.find('div', {'class': 'job-info'}).get_text(strip=True, separator='\n').splitlines()
    #print(job_info_raw)
    job_desc = soup.find('div', {'id': 'jobDesc'}).get_text(strip=True)
    job_info = {}
    for i in range(0, len(job_info_raw)-1, 2):
        job_info[job_info_raw[i].replace(':', '').replace(';', '')] = job_info_raw[i+1]

    if '' in job_info:
        del job_info['']
    #print(job_info)
    job_info['job_title'] = job_title
    job_info['institution'] = institution
    job_info['location'] = location
    job_info['job_desc'] = job_desc.replace(':', '')
    print(job_title)
    return job_info

job_detail_list = []
count = 0
for job_detail_link in jobs_batch[:100]:
    job_detail = scrape_higheredjobs_detail_page(jobs_batch[count])
    print(count, end=' ')
    count += 1

time.sleep(120)
count = 0
for i in async_link:
    job_detail = scrape_jobs(i)
    job_detail_list.append(job_detail)
    print(count, end=' ')
    count += 1


import pandas as pd


df = pd.read_json(json.dumps(job_detail_list))

df.to_csv('/Users/jaykakadiya/upwork/Vik/output/output_'+str(start_row)+'.csv', index=False, header=False)
print('output_'+str(start_row)+'.csv')
