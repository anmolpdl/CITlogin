import time
import sys
from selenium import webdriver
import configparser

def getDetails():
        Config = configparser.ConfigParser()
        Config.read("acc.ini") #single section Account and options Username, Password, Waittime
        try:
                details_list = [Config.get("Account", x) for x in ["Username", "Password", "Waittime"]]
                if not all(details_list):
                        raise Exception
        except Exception as e:
                print(e)
                sys.exit()

        else:
                return details_list

def login(acctuple):
        #need relevant webdriver in PATH, add and modify as needed
	browser = webdriver.Chrome()

	#subject to change if redirected login page changes
	browser.get('http://10.100.1.1:8090/')

        #waiting time to allow loading
	time.sleep(int(acctuple[2]))

	#entering in username box
	user = browser.find_element_by_css_selector('#usernametxt > td > input')
	user.send_keys(acctuple[0])

	#entering in password box
	password = browser.find_element_by_css_selector('body > form > div.maindiv > div.datablock > div.tablecss > table > tbody > tr:nth-child(4) > td > input')
	password.send_keys(acctuple[1])

	#finally clicking
	login = browser.find_element_by_css_selector('#logincaption')
	login.click()

def main():
        sys.stdout.write('Logging in...')
        time.sleep(1)
        acctuple = getDetails()
        login(acctuple)
        sys.stdout.write('You have logged in')
        time.sleep(1)

if __name__ == '__main__':
        main()
