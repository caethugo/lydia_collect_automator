from selenium import webdriver
from selenium.webdriver.common.keys import Keys #used to simulate some keyboard keys (Alt, Tab, etc.)
from selenium.webdriver.common.by import By #used to locate elements on website
import time
from selenium.webdriver.chrome.options import Options #We need this to prevent notifications and pop-ups
import os #Can be useful to get one's credentials without putting them in clear text