'''This program is used to download a pdf of the Philadelphia Inquirer.
   The program downloads the PDF, copies the file to a special folder, and
   creates a desktop shortcut.
   It is personalized for myself, Timothy Payne Jr.
   There are three main components:
   1. Downloading
   2. Cutting/Pasting
   3. Desktop Shortcut'''

import selenium
import os
import time
import datetime
import glob
import shutil
import os, winshell
from win32com.client import Dispatch
import sys
from selenium import webdriver

#Part 1 - Downloading the pdf

chrome_path = r"C:\bin\chromedriver.exe"
options = webdriver.ChromeOptions()
browser = webdriver.Chrome(chrome_path, chrome_options = options)
browser.get(r'https://www.inquirer.com/')
time.sleep(10)

login = browser.find_element_by_xpath('//*[@id="desktop-login-btn"]')
login.click()
time.sleep(10)

email = browser.find_element_by_xpath('//*[@id="auth0-lock-container-1"]/div/div[2]/form/div/div/div[3]/span/div/div/div/div/div/div/div/div/div[2]/div[1]/div/input')

#use whatever method to retrieve encrypted un
email.send_keys('<username>')
password = browser.find_element_by_xpath('//*[@id="auth0-lock-container-1"]/div/div[2]/form/div/div/div[3]/span/div/div/div/div/div/div/div/div/div[2]/div[2]/div[1]/div/input')

#use whatever method to retrieve encrypted pass
password.send_keys('<password>')
login = browser.find_element_by_xpath('//*[@id="auth0-lock-container-1"]/div/div[2]/form/div/div/button/span')
login.click()
time.sleep(10)

digital_edition = browser.find_element_by_xpath('/html/body/div[1]/section/div[2]/footer/div/div[2]/div[1]/div/div[2]/div/div[1]/div/a/div')
browser.execute_script("(arguments[0]).click();", digital_edition)
time.sleep(10)

#sometimes it was taking me to a random add... this script would bypass that if necessary
try:
	cancel = browser.find_element_by_xpath('/html/body/div[35]/div[1]/div/div/div[3]/a[1]')
	cancel.click()

except:
        pass


save_as_pdf = browser.find_element_by_xpath('/html/body/div[2]/div/div[6]/div[4]/div[1]/div/div[5]')
browser.execute_script("(arguments[0]).click();", save_as_pdf)
ok = browser.find_element_by_xpath('//*[@id="HtmlTag"]/body/div[21]/div[11]/div[1]')
ok.click()

#Part 2 - Moving the file
#adjust this for your own directories

list_of_files = glob.glob('<directory>') # * means all if need specific format then *.csv
dir_len = len(list_of_files)

while len(list_of_files)==dir_len:    
    list_of_files = glob.glob('<directory>')

else:    
	latest_file = max(list_of_files, key=os.path.getctime)
	print(latest_file)
	shutil.move(latest_file,'<intended destination>')

#Part 3 - Creating a Desktop Shortcut
#again, adjust for your own directories.
desktop = winshell.desktop()
path = os.path.join(desktop, "<name your shortcut here>.lnk")
list_of_files = glob.glob('<location of file>')
latest_file = max(list_of_files, key=os.path.getctime) # * means all if need specific format then *.csv
target = latest_file
wDir = "<location of file>"
icon = "<directory of shortcut icon>"
shell = Dispatch('WScript.Shell')
shortcut = shell.CreateShortCut(path)
shortcut.Targetpath = target
shortcut.WorkingDirectory = wDir
shortcut.IconLocation = icon
shortcut.save()
browser.quit()
sys.exit()
