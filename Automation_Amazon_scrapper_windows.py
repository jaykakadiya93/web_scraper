from selenium import webdriver
import time
from re import search
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox
from csv import reader
import platform
from tkinter.filedialog import askopenfilename, askdirectory
import datetime
from datetime import timezone


def _start_scrapper():
    dt = datetime.datetime.now() 
  
    utc_time = dt.replace(tzinfo = timezone.utc) 
    utc_timestamp = utc_time.timestamp()
    messagebox.showinfo("Input File", "Select Input File")
    file_in=askopenfilename(filetypes =[('csv file', '*.csv')])
    print(file_in)
    input_filename_with_extension= file_in.split("/")
    input_file=(input_filename_with_extension[len(input_filename_with_extension)-1]).split('.')

    messagebox.showinfo("Output folder", "Select Output Folder")
    out_path=askdirectory(title='Select Folder')
    file_out = open(out_path+"/"+str(input_file[0]).replace(" ","_")+str(utc_timestamp).replace(" ","_")+".csv", "w", encoding="utf-8")
    file_out.write("Brand,Product URL,Sold By,Business Name,Address_1,Address_2,Address_3,Address_4,Address_5,Address_6,Address_7" + '\n')
    driver = webdriver.Chrome()
    count=0
    delimiter=','

    try:
        with open(file_in) as x:
            for line in reader(x):
                if line[0] != '' and count != 0:
                    
                    driver.get(str(line[1]).strip())
                    #time.sleep(2)
                    try:
                        link=''
                        business_name=''
                        address_1=''
                        address_2=''
                        address_3=''
                        address_4=''
                        address_5=''
                        address_6=''
                        address_7=''
                        b_name=''
                        link=driver.find_element_by_xpath("//*/div[@id='buybox-tabular']//*/tbody/tr[2]/td[2]/span").text
                        driver.find_element_by_xpath("//*/div[@id='buybox-tabular']//*/a").send_keys(Keys.ENTER)
                        #driver.find_element_by_xpath("//*/tbody/tr[2]").click()
                        time.sleep(2)
                        business_name = driver.find_element_by_xpath("//*/ul[@class='a-unordered-list a-nostyle a-vertical']/li/span").text
                        business_name=business_name.split(":")
                        b_name=business_name[1]
                        address_1 = driver.find_element_by_xpath("//*/ul[@class='a-unordered-list a-nostyle a-vertical']/li[2]/span/ul/li/span").text
                        
                        address_2 = driver.find_element_by_xpath("//*/ul[@class='a-unordered-list a-nostyle a-vertical']/li[2]/span/ul/li[2]/span").text
                        address_3 = driver.find_element_by_xpath("//*/ul[@class='a-unordered-list a-nostyle a-vertical']/li[2]/span/ul/li[3]/span").text
                        address_4 = driver.find_element_by_xpath("//*/ul[@class='a-unordered-list a-nostyle a-vertical']/li[2]/span/ul/li[4]/span").text
                        address_5 = driver.find_element_by_xpath("//*/ul[@class='a-unordered-list a-nostyle a-vertical']/li[2]/span/ul/li[5]/span").text
                        address_6 = driver.find_element_by_xpath("//*/ul[@class='a-unordered-list a-nostyle a-vertical']/li[2]/span/ul/li[6]/span").text
                        address_7 = driver.find_element_by_xpath("//*/ul[@class='a-unordered-list a-nostyle a-vertical']/li[2]/span/ul/li[7]/span").text

                        string = "\""+line[0]+"\""+delimiter+"\""+line[1]+"\""+delimiter+"\""+link+"\""+\
                            delimiter+"\""+b_name+"\""+delimiter+\
                            "\""+address_1+"\""+delimiter+"\""+address_2+"\""+delimiter\
                                +"\""+address_3+"\""+delimiter+\
                            "\""+address_4+"\""+delimiter+"\""+address_5+"\""+delimiter+\
                                "\""+address_6+"\""+delimiter+"\""+address_7+"\""
                        
                        file_out.write(string + '\n')
                        
                        
                    except (NoSuchElementException,ElementNotInteractableException) as e:
                        
                        string = "\""+line[0]+"\""+delimiter+"\""+line[1]+"\""+delimiter+"\""+link+"\""+\
                            delimiter+"\""+b_name+"\""+delimiter+\
                            "\""+address_1+"\""+delimiter+"\""+address_2+"\""+delimiter\
                                +"\""+address_3+"\""+delimiter+\
                            "\""+address_4+"\""+delimiter+"\""+address_5+"\""+delimiter+\
                                "\""+address_6+"\""+delimiter+"\""+address_7+"\""
                        file_out.write(string + '\n')
                        
                    count=count+1
                count=count+1

        file_out.close()
        messagebox.showinfo("Amazon Scrapper", "Success")
    except Exception as e:
        file_out.close()
        messagebox.showinfo("Amazon Scrapper", e)
       
gui = Tk(className='Jungle scout')
gui.geometry("300x300")
Button(gui, text ='start Amazon Scrapper',font=("Helvetica", 20),height = 10, width = 30, command = lambda:_start_scrapper()).pack()
gui.mainloop()
