from selenium import webdriver
from selenium.webdriver.common.keys import Keys #used to simulate some keyboard keys (Alt, Tab, etc.)
from selenium.webdriver.common.by import By #used to locate elements on website
import time
from selenium.webdriver.chrome.options import Options #We need this to prevent notifications and pop-ups
from selenium.common.exceptions import NoSuchElementException #to try and catch the error we need to import it !
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities #This will enable us not to wait until the page is fully loaded with .get()

def nonotif_driver_init(path_to_chrome_driver, link) :
    #About blocking those pop-up notifications
    option = Options()
    option.add_argument("--disable-infobars")
    option.add_argument("start-maximized")
    option.add_argument("--disable-extensions")
    # Pass the argument 1 to allow and 2 to block
    option.add_experimental_option("prefs", { 
        "profile.default_content_setting_values.notifications": 2
    })

    #About not wanting a page to fully load
    caps = DesiredCapabilities().CHROME
    caps["pageLoadStrategy"] = "none"   # Just wait until page is interactive

    driver = webdriver.Chrome(desired_capabilities=caps, chrome_options=option, executable_path='/Users/hugocaetano/Desktop/lydia_collect_automator/chromedriver')
    driver.get(link) 
    return driver

def fb_cookie_accepter(driver) :
    cook = driver.find_element(By.XPATH, "//button[@data-cookiebanner='accept_only_essential_button']")
    cook.click()
    return("The essential cookies should now be accepted")


def facebook_logger(driver, user, pwd) :
    #finding elements
    mail = driver.find_element(By.ID, "email")
    password = driver.find_element(By.ID, "pass")
    #inputing credentials
    mail.send_keys(user)
    password.send_keys(pwd)
    #clicking on login (french fb)
    clicker = driver.find_element(By.XPATH, "//input[@value='Se connecter']") #actually this id changes each time so I need another solution...
    clicker.click() 
    return("No problem occured during the logging in")


def pagewatcher(waitingtime = 90, step = 5, link = "collecte.io", driver = None) :
    """This function looks """
    if driver is None :
        driver = global_driver #to get around default parameter name not defined
    time0 = time.time()
    while time.time() - time0 < waitingtime :
        try : 
            lydia = driver.find_element(By.CSS_SELECTOR, "a[href*='" + link + "']")
            lydia = lydia.get_attribute('href') #strange looking operation to get the link returned and not a driver, for speed purposes
            print("the link is clicked on")#Here we would call the lydia form filler function but we need to make it work together first
            m = 1
            break #if we find the link, stop looking for it 
        except NoSuchElementException :
            print("The link you provided was not found.")
            m = 2
            driver.refresh() #if we don't refresh, we won't see the new posts
        time.sleep(step)
    if m == 1 :
        print("it seems like we can complete the form")
        return(lydia)
    elif m == 2 :
        return("The link was never found")


def true_completer(driver, dic):
    """The completer function completes all fields from the dictionary in the elements wich are linked to the 
    labels list's elements. If there is no field that corresponds to an element in dic, it won't return an error 
    message. Then, 'mieux vaut trop que pas assez'"""
    was_completed = []
    path = '//div/label'
    elements = driver.find_elements(By.XPATH, path)
    for i in list(dic.keys()) :
        for j in elements:
            path_j = "//*[@id='" + j.get_attribute('for') + "']"
            element_j = driver.find_element(By.XPATH, path_j) #getting the element associated with the j-th label
            if i in j.text:
                if not "\n" in element_j.text : #it is a text input
                    element_j.clear() #we clear all potential text in the input element
                    attrib_ij = dic.get(i)
                    element_j.send_keys(attrib_ij)  
                elif "\n" in element_j.text : #it is a scrolling menu 
                    attrib_ij = dic.get(i) #it is the value we want to select
                    menu_el_path_i = "//option[@value='" + attrib_ij + "'" #we find the clickable element
                    option_i = element_j.find_element(By.XPATH, navette_path) #we need to find IN the selector we already have
                    option_i.click()
                was_completed.append(j)
    uncomp = list(set(elements) - set(was_completed)) #all untouched elements
    for k in uncomp : #We'll complete all empty fields ! Else we won't be able to sumbit the form
        path_k = "//*[@id='" + k.get_attribute('for') + "']"
        uncomp_k = driver.find_element(By.XPATH, path_k)
        if not "\n" in uncomp_k.text : #it is a text input
                    uncomp_k.clear() #we clear all potential text in the input element
                    uncomp_k.send_keys("Jsp") #means I don't know in french : it is the case !
        elif "\n" in uncomp_k.text : #it is a scrolling menu 
            first_option_path_k = path_k + "/option[2]" #it's safe bc first option is title and even if no title, two options at minimum
            first_option_k = uncomp_k.find_element(By.XPATH, first_option_path_k)
            first_option_k.click()
    return("The form was completed without problem")
