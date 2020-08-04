from selenium import webdriver
import bs4
from bs4 import BeautifulSoup
import time
from re import search
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


counter=0
delimiter="|"
output = []
name_list=[]
name=''
office_name=''
phone=''
email=''

header = "name"+delimiter+"office_name"+delimiter+"phone"+delimiter+"email"



#session_id='3b347c8196a97469f9b752cbb3d78f85'
#executor_url='http://127.0.0.1:55821'
driver = webdriver.Chrome()
#driver = webdriver.Remote(command_executor=executor_url, desired_capabilities={})
#driver.session_id = session_id
executor_url = driver.command_executor._url
session_id = driver.session_id
print(executor_url)
print(session_id)

driver.get("https://idp.armls.com/account/login")

elementID = driver.find_element_by_id('Username')
elementID.send_keys('uname')
elementID = driver.find_element_by_id('Password')
elementID.send_keys('Passw')
elementID.submit()

driver.get('https://armls.flexmls.com/')

driver.get('https://apps.flexmls.com/people/accounts')

driver.find_element_by_class_name('membersTabTrigger').click()
time.sleep(5)

while True:

    
    source_code = BeautifulSoup(driver.page_source,features="lxml")
    condition = source_code.find_all("span",{"class":"u-overflow-ellipsis"})
    #print(len(condition))
    if len(condition) >= counter:
        for x in range(counter, 40000):
            if counter == len(condition):
                source_code = BeautifulSoup(driver.page_source,features="lxml")
                condition = source_code.find_all("span",{"class":"u-overflow-ellipsis"})
            name = source_code.find_all("span",{"class":"u-overflow-ellipsis"})[counter].text.strip()
            

            driver.find_element_by_xpath("//span[text()=\""+name+"\"]").click()
            time.sleep(1.5)
            #element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "memberDetailsModal")))

            # panel_code = BeautifulSoup(driver.page_source,features="lxml")
            # code = panel_code.find_all("div",{"details-modal-group"})
            #office_name = panel_code.find("a",{"u-link--plain officeModalSwitcher"}).text.strip()
            office_name = driver.find_element_by_class_name('officeModalSwitcher').text
            try:
                phone = driver.find_element_by_xpath("//div[@class='details-modal-group']//div[text()='Mobile']/following-sibling::div").text
                
            except NoSuchElementException:
                print('exception')
            try:
                email = driver.find_element_by_xpath("//div[@class='details-modal-group']//div[text()='Email']/following-sibling::div").text
                
            except NoSuchElementException:
                print('exception')


            with open('output_1.txt', 'a') as filehandle:
                filehandle.write(name+delimiter+office_name+delimiter+phone+delimiter+email+'\n')
            phone=''
            email=''
            code=''
            panel_code=''
            time.sleep(1)
            webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
            counter = counter + 1
            if counter == len(condition):
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                #time.sleep(2)
    else:
        # counter = counter + 1
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
