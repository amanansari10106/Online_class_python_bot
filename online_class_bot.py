from selenium import webdriver
import pyautogui
import time
from time import sleep

        

# Defining functions for the digital electrnic class
 

def function_for_de_class(j) :
    k = 0
    while k == 0 :
        time.sleep(4)
        driver.get("https://teams.microsoft.com/_#/school/conversations/General?threadId=19:d5f43fd2e50240c386a0547039709c3a@thread.tacv2&ctx=channel")
        time.sleep(4)
        driver.get("https://teams.microsoft.com/_#/school/conversations/General?threadId=19:d5f43fd2e50240c386a0547039709c3a@thread.tacv2&ctx=channel")
        print("its done 1")
        time.sleep(100)
        print("its done 2")
        try:
            driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div/div/calendar-dialog-bridge/div/div[1]/div[2]/button[1]").click()
        
        except Exception:
            print("no de class now") 
            break   

        print("its done 3")
        pyautogui.press('tab')
        time.sleep(1)
        pyautogui.press('tab')
        time.sleep(1)
        pyautogui.press('tab')      
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(8)
        pyautogui.press('enter')
        time.sleep(10)
        driver.find_element_by_id('hangup-button').click()
        time.sleep(5)
        classesleft.pop(j)
        k = k+1

# Defining functions for the math class


def function_for_math_class(j) :
    k = 0
    while k == 0 :
        time.sleep(4)
        driver.get("https://teams.microsoft.com/_#/school/conversations/General?threadId=19:dc6af8d3ba7f49a7a7f101141c96c405@thread.tacv2&ctx=channel")
        time.sleep(4)
        driver.get("https://teams.microsoft.com/_#/school/conversations/General?threadId=19:dc6af8d3ba7f49a7a7f101141c96c405@thread.tacv2&ctx=channel")
        print("its done 1")
        time.sleep(100)
        print("its done 2")
        try:
            driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div/div/calendar-dialog-bridge/div/div[1]/div[2]/button[1]").click()
        
        except Exception:
            print("no math class now")
            break 

        print("its done 3")
        pyautogui.press('tab')
        time.sleep(1)
        pyautogui.press('tab')
        time.sleep(1)
        pyautogui.press('tab')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(8)
        pyautogui.press('enter')
        time.sleep(10)
        driver.find_element_by_id('hangup-button').click()
        classesleft.pop(j)
        k = k+1

# Defining functions for the Data structure and algorthm class

def function_for_dsalgo_class(j) :
    k = 0
    while k == 0 :
        time.sleep(4)
        driver.get("https://teams.microsoft.com/_#/school/conversations/General?threadId=19:67316d95a1974bf087b8a641304cac7d@thread.tacv2&ctx=channel")
        time.sleep(4)
        driver.get("https://teams.microsoft.com/_#/school/conversations/General?threadId=19:67316d95a1974bf087b8a641304cac7d@thread.tacv2&ctx=channel")
        print("its done 1")
        time.sleep(100)
        print("its done 2")
        try:
            driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div/div/calendar-dialog-bridge/div/div[1]/div[2]/button[1]").click()
        
        except Exception:
            print("no dsalgo class now") 
            break

        print("its done 3")
        pyautogui.press('tab')
        time.sleep(1)
        pyautogui.press('tab')
        time.sleep(1)
        pyautogui.press('tab')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(8)
        pyautogui.press('enter')
        time.sleep(10)
        driver.find_element_by_id('hangup-button').click()
        classesleft.pop(j)
        k = k+1
   

# Defining functions for the ppl class

def function_for_ppl_class(j) : 
    k = 0
    while k == 0 :
        time.sleep(4)
        driver.get("https://teams.microsoft.com/_#/school/conversations/General?threadId=19:db4165a102ca4cc280ff397cfa1c763e@thread.tacv2&ctx=channel")
        time.sleep(4)
        driver.get("https://teams.microsoft.com/_#/school/conversations/General?threadId=19:db4165a102ca4cc280ff397cfa1c763e@thread.tacv2&ctx=channel")
        print("its done 1")
        time.sleep(100)
        print("its done 2")
        try:
            driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div/div/calendar-dialog-bridge/div/div[1]/div[2]/button[1]").click()
        
        except Exception:
            print("no ppl class now") 
            break

        print("its done 3")
        pyautogui.press('tab')
        time.sleep(1)
        pyautogui.press('tab')
        time.sleep(1)
        pyautogui.press('tab')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(8)
        pyautogui.press('enter')
        time.sleep(10)
        driver.find_element_by_id('hangup-button').click()

        classesleft.pop(j)
        k = k+1


# Defining functions for the Operatng system class class

def function_for_os_class(j) :
    k = 0
    while k == 0 :
        time.sleep(4)
        driver.get("https://teams.microsoft.com/_#/school/conversations/General?threadId=19:587e58b4649e45dfbc85d6faaad1e9ba@thread.tacv2&ctx=channel")
        time.sleep(4)
        driver.get("https://teams.microsoft.com/_#/school/conversations/General?threadId=19:587e58b4649e45dfbc85d6faaad1e9ba@thread.tacv2&ctx=channel")
        print("its done 1")
        time.sleep(100)
        print("its done 2")
        try:
            driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div/div/calendar-dialog-bridge/div/div[1]/div[2]/button[1]").click()
        
        except Exception:
            print("no os class now") 
            break

        print("its done 3")
        pyautogui.press('tab')
        time.sleep(1)
        pyautogui.press('tab')
        time.sleep(1)
        pyautogui.press('tab')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(8)
        pyautogui.press('enter')
        time.sleep(10)
        driver.find_element_by_id('hangup-button').click()
        classesleft.pop(j)
        k = k+1


# Defining variables

classesleft = ["de" , "math" , "ppl" , "os" , "dsalgo"]
i = 0

                             ################### EXECUTION STARTS #####################




# Taking username and password as a input from the user

username = input("Enter Username")
passowrd = input("Enter Password")


# Defining driver variable

driver = webdriver.Chrome('D:\mychromedriver\chromedriver_win32\chromedriver.exe')

# Opening the Microsoft teams website for login

driver.get("https://login.microsoftonline.com/common/oauth2/authorize?response_type=id_token&client_id=5e3ce6c0-2b1f-4285-8d4b-75ee78787346&redirect_uri=https%3A%2F%2Fteams.microsoft.com%2Fgo&state=7ab16a85-c363-4c59-b60f-52c48f19f3bf&&client-request-id=f86b52c0-55b7-400c-9860-ee864eb44448&x-client-SKU=Js&x-client-Ver=1.0.9&nonce=dc93b7de-2309-4a10-9529-defb83b18412&domain_hint=")
sleep(3)

# Inputing username and password and completing login 
pyautogui.write(username)  
pyautogui.press('enter') 

time.sleep(10)
pyautogui.write(passowrd)
pyautogui.press('enter')
time.sleep(3)
pyautogui.press('enter')
time.sleep(8)
driver.get("https://teams.microsoft.com/_?culture=en-in&country=IN&lm=deeplink&lmsrc=homePageWeb&cmpid=WebSignIn#/school/conversations/General?threadId=19:587e58b4649e45dfbc85d6faaad1e9ba@thread.tacv2&ctx=channel")
#####


######## Main logic for the program to ateend classes ######



while i<5 :
    if classesleft[i] == "de" :
        function_for_de_class(i)
        i = i+1
        continue
    if classesleft[i] == "math" : 
        function_for_math_class(i)
        i = i+1
        continue
    if classesleft[i] == "ppl" :
        function_for_ppl_class(i)
        i = i+1
        continue
    if classesleft[i] == "os":
        function_for_os_class(i)
        i = i+1
        continue
    if classesleft[i] == "dsalgo" :
        function_for_dsalgo_class(i)
        i = i+1
        continue



