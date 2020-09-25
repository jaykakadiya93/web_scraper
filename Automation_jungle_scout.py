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
from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox



def _start_scrapper():
    try:

        catagory_id=simpledialog.askstring(title="User Input",
                                    prompt="Enter Catagorey id")
        star_price=simpledialog.askstring(title="User Input",
                                    prompt="Enter starting cost")
        end_price=simpledialog.askstring(title="User Input",
                                    prompt="Enter ending cost")
        page=simpledialog.askstring(title="User Input",
                                    prompt="Enter pages")
        chromeOptions = webdriver.ChromeOptions()
        prefs = {"download.default_directory" : "/Users/jkakad407/Downloads/jungle"}
        chromeOptions.add_experimental_option("prefs",prefs)
        #chromedriver = "path/to/chromedriver.exe"
        #driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=chromeOptions)
        driver = webdriver.Chrome(chrome_options=chromeOptions)


        executor_url = driver.command_executor._url
        session_id = driver.session_id
        print(executor_url)
        print(session_id)

        driver.get("https://members.junglescout.com/?_ga=2.214201362.427976688.1599509107-324072684.1599353207#/login?redirectRoute=/database")

        elementID = driver.find_element_by_xpath("//div[@class='login__form']/input[1]")
        elementID.send_keys('')
        elementID = driver.find_element_by_xpath("//div[@class='login__form']/input[2]")
        elementID.send_keys('')


        driver.find_element_by_class_name('ButtonWrapper-sc-1vti96x-0').click()
        time.sleep(5)
        driver.find_element_by_class_name('ktEcCj').click()
        time.sleep(3)
        driver.find_element_by_class_name('gNQCOx').click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[@class='CardWrapper-sc-1xay5eh-0 bLHPDY card-section filters__column filters__column--mini']/div[@class='SellerTypeSelectWrapper-sc-1c6xldc-0 cgTvsL filters__row']/div[@class='checkbox-group'][2]").click()

        driver.find_element_by_xpath("//div[@class='CardWrapper-sc-1xay5eh-0 ibmOSQ card-section filters__section']/div[@class='CategorySelectWrapper-jr7gs7-0 evJdIA']/div["+str(catagory_id)+"]").click()

        driver.find_element_by_xpath("//div[@class='CardWrapper-sc-1xay5eh-0 bLHPDY card-section filters__section']/div[2]/div/input[1]").send_keys(str(star_price))
        driver.find_element_by_xpath("//div[@class='CardWrapper-sc-1xay5eh-0 bLHPDY card-section filters__section']/div[2]/div/input[2]").send_keys(str(end_price))
        driver.find_element_by_xpath("//div[@class='filters filters--database']/div[@class='SearchSection-sc-1iuvgd5-1 jIQawl']/div/button[2]").click()
        time.sleep(10)
        driver.find_element_by_xpath("//div[@class='filters filters--database']/div[@class='SearchSection-sc-1iuvgd5-1 jIQawl']/div[2]/button").send_keys(Keys.ENTER)


        for i in range(2, int(page), 1):
            driver.find_element_by_xpath("//div[@class='database']/div[3]/div/div[2]/div[2]/div/input").clear()
            driver.find_element_by_xpath("//div[@class='database']/div[3]/div/div[2]/div[2]/div/input").send_keys(str(i))
            driver.find_element_by_xpath("//div[@class='database']/div[3]/div/div[2]/div[2]/div/input").send_keys(Keys.ENTER)
            time.sleep(5)
            driver.find_element_by_xpath("//div[@class='filters filters--database']/div[@class='SearchSection-sc-1iuvgd5-1 jIQawl']/div[2]/button").send_keys(Keys.ENTER)
        time.sleep(3)
        driver.quit()
        messagebox.showinfo("Jungle scout", "Success")
    except Exception as e:
        messagebox.showinfo("Jungle scout fail", e)
       
gui = Tk(className='Jungle scout')
gui.geometry("300x300")
Button(gui, text ='start file download process',font=("Helvetica", 20),height = 10, width = 30, command = lambda:_start_scrapper()).pack()
gui.mainloop()