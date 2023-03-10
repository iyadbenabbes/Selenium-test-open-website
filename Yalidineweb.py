import time
import requests
from bs4 import BeautifulSoup
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd


driver = webdriver.Firefox()


def login(email_, password_):
    driver.get("https://yalidine.app/app/login.php")

    email = driver.find_element(By.NAME, 'email')
    password = driver.find_element(By.NAME, 'password')

    email.click()
    email.send_keys(email_)
    time.sleep(1)

    password.click()
    password.send_keys(password_)
    time.sleep(1)
    log_in = driver.find_element(By.ID, 'connectButton')
    log_in.click()
    time.sleep(4)


login('benabbes.iyad@gmail.com', 'espn9090')


def sales_section():
    sales = driver.find_element(By.XPATH, '/html/body/nav/div[2]/li')
    sales.click()
    time.sleep(1)
    sales_view = driver.find_element(
        By.XPATH, "/html/body/nav/div[2]/li/div/a[2]")
    sales_view.click()
    time.sleep(1)
    click = driver.find_element(
        By.XPATH, '/html/body/div[3]/form[2]/div[2]/table/tbody/tr[1]/td[2]/button')


sales_section()
