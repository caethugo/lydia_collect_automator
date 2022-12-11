#This file is meant to achieve all tasks from going to a facebook page and logging in to completing the form and submitting it

##Importing all useful modules and functions. I chose not to import dependencies because it makes the code less readable
import os #Can be useful to get one's credentials without putting them in clear text
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities #because of our last step
import functions as fun #our own file, containing all needed dependencies

##Storing my credentials and defining all useful variables for my shotgun
path_to_driver = "/Users/hugocaetano/Desktop/lydia_collect_automator/chromedriver" #You need a chromedriver to navigate through webpages
link = "https://fb.me/e/2e7mRxvMx" #replace this link by the link of the facebook event you want to navigate through
user = os.getenv("fb_user") #you just need to store your user email address 
pwd =os.getenv("fb_pwd") #and password
dic = { #Here you have to give your personal pieces of information that could be required in the form
    'Nom' : 'Caetano',
    'Prénom' : 'Hugo',
    'Numéro de téléphone' : '0619372524',
    'Adresse email' : 'hugocaetano78800@gmail.com',
    'Asso' : 'BDX',
    'Numéro étudiant' : '20213566',
    'Promo' : '3A'
}

##Constructing complete driver and access fb page
driver = fun.nonotif_driver_init(path_to_chrome_driver = path_to_driver, link = link)


##Accept cookies to be able to navigate through the page
fun.fb_cookie_accepter(driver = driver)

##Connection to facebook 
fun.facebook_logger(driver = driver, user = user, pwd = pwd)


##Starting to watch link in page
lydia_link = fun.pagewatcher(waitingtime = 90, step = 2, link = "collecte.io", driver = driver)
print("The lydia collect link was stored")

##Complete it

###We design a fast reacting driver
caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "none"
driver2 = webdriver.Chrome(desired_capabilities=caps, executable_path='/Users/hugocaetano/Desktop/lydia_collect_automator/chromedriver')
driver2.get(lydia_link)
fun.true_completer(driver = driver2, dic = dic)
print("The lydia form was completed")
#Then submit it ! Note that not submitting it can be safer because some inputs could be unexpected in the lydia form !
#submit = lydia_driver.find_element(By.ID, 'submit-state-lydia') #finding the submit button
#submit.click()
