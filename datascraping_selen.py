#COLETA DE DADOS E ENVIO DE EMAILS
#site do BANCO CENTRAL - HISTORICO DO DOLLAR
#https://www.cobasi.com.br/

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.cobasi.com.br/') 

search_google = driver.find_element(By.XPATH, '//html/body/div/form/div/input').click()
cotdollar = driver.find_element(By.XPATH, '/html/body/div/table/tbody/tr[3]')


dollartext = cotdollar.text
print(dollartext)
