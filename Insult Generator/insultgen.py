#title           :insultgen.py
#description     :Generates insults based on name given using the website intellisult.com
#author          :Harsimran Grewal (Retr0-Flow on github)
#date            :20/8/2019
#version         :3.0
#usage           :To generate a specified amount (default 10000) insults for someone
#notes           : This is essentialy a scrapper that goes to a website and uses it to get a lot of i.nsults for someone you might not like.
#python_version  :3.7.0
#==============================================================================


import time
import asyncio
import threading
from selenium import webdriver

"""
site = 'http://intellisult.com/'
file_to_write = open('C:\\Users\\Henry\\Desktop\\insults.txt', 'a')
x = 0
br = webdriver.Firefox()
br.implicitly_wait(5)
br.get(site)
search = br.find_element_by_id('intellisultName')
search.send_keys('NAME')
while x < 10000:
    x += 1
    search = br.find_element_by_id('intellisultDo')
    search.click()
    time.sleep(1.5)
    search = br.find_element_by_id('intellisultInsult')
    result = str(search.text)
    file_to_write.write(str(result) + '\n')
    print(x)
br.close()
file_to_write.close()
"""



