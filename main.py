"""
#DAY1
I will Try to detect the register button and click on it
lets GOOOO
"""
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
by = By()
driver = webdriver.Chrome(executable_path="/home/walid/Bureau/EcandidatAutomate/chromedriver")
driver.get("https://ecandidat-2021.univ-lille.fr/#!accueilView")
