import csv
from selenium.webdriver import Chrome, ChromeOptions, Remote
from selenium.webdriver.common.keys import Keys
import lxml.html
import requests
import time
import re
from selenium.webdriver.common.action_chains import ActionChains


def main():
	try:
		mail_address = 's.hikaru.yakyu.0823@gmail.com'
		password = 'hikaru0823'

		
		options=ChromeOptions()
		options.headless=True
		
		options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 6.1; WOW64; rv:25.0) Gecko/20100101 Firefox/25.0')
		driver=Chrome(options=options)
		

		url = 'https://accounts.google.com/signin/v2/identifier?hl=ja&passive=true&continue=https%3A%2F%2Fwww.google.com%2Fwebhp%3Fhl%3Dja%26sa%3DX%26ved%3D0ahUKEwj9jtHspq3vAhUCEqYKHYZ4D84QPAgI&ec=GAZAmgQ&flowName=GlifWebSignIn&flowEntry=ServiceLogin'
		driver.get(url)
		
		driver.save_screenshot('colb.png')
		element = driver.switch_to.active_element
		element.send_keys(mail_address)
		element.send_keys(Keys.ENTER)
		#driver.find_element_by_id("identifierID").send_keys(mail_address)
		driver.save_screenshot('colb.png')
		
		time.sleep(60)
		driver.save_screenshot('colb.png')
		driver.find_element_by_name("password").send_keys(password)
		driver.find_element_by_id("passwordNext").click()

		url='https://colab.research.google.com/drive/1F18kintNY67aG_8LoOdnhuiQtLux7Pqw?usp=sharing'

		driver.find_element_by_id("input").send_keys(url)
		driver.find_element_by_id("icon").click()
		
		

		
		driver.save_screenshot('colb.png')
		driver.find_element_by_xpath('//*[@id="runtime-menu-button"]/div/div/div[1]').click()
		driver.find_element_by_xpath('//*[@id=":1w"]/div').click()
		driver.save_screenshot('click_colb.png')
		driver.quit()
	except:
		print("error")
		import traceback
		traceback.print_exc()
		driver.quit()
	
if __name__=="__main__":
	main()