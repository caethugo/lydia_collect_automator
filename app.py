#This file is meant to achieve all tasks from going to a facebook page and logging in to completing the form and submitting it

##Importing all useful modules and functions. I chose not to import dependencies because it makes the code less readable
import os #Can be useful to get one's credentials without putting them in clear text
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities #because of our last step
import functions as fun #our own file, containing all needed dependencies
import streamlit as st
#dictionnary handling
import json 
from streamlit_ace import st_ace


def app():
    try:
        #Storing the credentials and defining all useful variables for the shotgun
        user = st.text_input("Facebook User Email Address", value = "john.deuf@gmail.com")
        pwd = st.text_input("Facebook Password", type="password")
        path_to_driver = "/Users/hugocaetano/Desktop/lydia_collect_automator/chromedriver" #You need a chromedriver to navigate through webpages
        link = st.text_input("Link to facebook page", value = "https://fb.me/e/2e7mRxvMx") 
        # Use a Multicolumn input field to allow the user to enter a dictionary
        json_string = st_ace(
            height=200,
            language="json",
            value=json.dumps({
                            'Nom' : 'Deuf',
                            'Prénom' : 'John',
                            'Numéro de téléphone' : '0619******',
                            'Adresse email' : 'jaune.deuf@gmail.com',
                            'Asso' : 'BD*',
                            'Numéro étudiant' : '2021****',
                            'Promo' : '3A'}),
                            theme="chrome",
        )

        # Convert the user input to a dictionary
        dic = json.loads(json_string)   
        
        #defining the two buttons to run the logging and the actual shotgun in different processes
        load_butt = st.button("Log in to FB and load the FB page")
        sg_butt = st.button("Process the shotgun") #to keep the driver active
        lydia_link = None #initializing the variable
        if load_butt :
            ##Constructing complete driver and access fb page
            driver = fun.nonotif_driver_init(path_to_chrome_driver = path_to_driver, link = link)

            ##Accept cookies to be able to navigate through the page
            fun.fb_cookie_accepter(driver = driver)

            ##Connection to facebook 
            fun.facebook_logger(driver = driver, user = user, pwd = pwd)

            ##Starting to watch link in page
            st.session_state.lydia_link = fun.pagewatcher(waitingtime = 90, step = 2, link = "collecte.io", driver = driver) #We need to store this value in the session !
            print("The pagewatcher() function has finished its job")
            ##We don't need the first driver anymore. Let's do this clean.
            driver.close() 

        if sg_butt :
            if "lydia_link" not in st.session_state : 
                st.error("Please load the FB page before processing the shotgun.")
            else:
                ###We design a fast reacting driver
                caps = DesiredCapabilities().CHROME
                caps["pageLoadStrategy"] = "eager" #waits for the page to be interactive
                driver2 = webdriver.Chrome(desired_capabilities=caps, executable_path='/Users/hugocaetano/Desktop/lydia_collect_automator/chromedriver')
                driver2.get(st.session_state.lydia_link)
                fun.true_completer(driver = driver2, dic = dic)
                print("The lydia form was completed")
                #Then submit it ! Note that not submitting it can be safer because some inputs could be unexpected in the lydia form !
                #submit = lydia_driver.find_element(By.ID, 'submit-state-lydia') #finding the submit button
                #submit.click()
                #driver2.close()

    except Exception as e:
        st.error("An error occurred: {}".format(e))

app()