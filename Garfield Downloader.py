'This script can be used to scrape'

import selenium
import urllib.request
import time
from datetime import date
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_path = r"C:\bin\chromedriver.exe"
options = webdriver.ChromeOptions()

browser = webdriver.Chrome(chrome_path, chrome_options = options,)
browser.get(r'https://garfield.com/comic/2007/06/19')

adult = browser.find_element_by_xpath('/html/body/div/table/tbody/tr/td/div/div/div/div[1]/div/div/div[2]/form/div[3]/label')
adult.click()
submit = browser.find_element_by_xpath('//*[@id="submit"]')
submit.click()

a=0
for x in range(732_846,737_554): #pre-determined ordinal dates

	comic_date = date.fromordinal(x)
	filename = str(comic_date.year)+'-'+('%02d' % comic_date.month)+'-'+('%02d' % comic_date.day)+'.gif'
	

	try:
		WebDriverWait(browser,60).until(
        EC.presence_of_element_located((By.XPATH,
                                        r'/html/body/div[2]/div[4]/div[3]/div[2]/div/img')))

	except:
		print(f"page stuck on {str(comic_date)}")

	comic = browser.find_element_by_xpath('/html/body/div[2]/div[4]/div[3]/div[2]/div/img')
	src = comic.get_attribute('src')
	urllib.request.urlretrieve(src,filename)
	next_com = browser.find_element_by_xpath('/html/body/div[2]/div[4]/div[3]/div[1]/div/div[1]/div/div[1]/div[2]/div[2]/a')
	next_com.click()

	a+=1
	print(a)
	if a == 150:


		new_date = date.fromordinal(x+1)
		y = str(new_date.year)
		m = '%02d' % new_date.month
		d ='%02d' % new_date.day
		browser.quit()
		browser = webdriver.Chrome(chrome_path, chrome_options = options,)
		time.sleep(5)
		browser.get(f'https:////garfield.com//comic//{y}//{m}//{d}')
		adult = browser.find_element_by_xpath('/html/body/div/table/tbody/tr/td/div/div/div/div[1]/div/div/div[2]/form/div[3]/label')
		adult.click()
		submit = browser.find_element_by_xpath('//*[@id="submit"]')
		submit.click()
		a=0
		continue

	else:
		continue

print('All Garfields have been saved.')