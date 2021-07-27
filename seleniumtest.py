#DESAFIO SELENIUM - automação Web com Python
#criação de bot e navega em um site específico

#instalando bibliotecas do Selenium no Python

#comando para dar um CTRL+A na página
#webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys("a").perform()


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://www.google.com.br/') 

#aqui é o comando para navegar no site do google

search_google = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')

#XPATH é o caminho do código

search_google.send_keys("Bolsas de Mulher" + Keys.ENTER)

#buscando pelo xpath do objeto que escolhi (através do inspecionar do Google
#usando o .click no final, eu consigo automatizar para clicar no
# objeto que eu quero
# 
search_google = driver.find_element(By.XPATH, '//*[@id="tads"]/div/div/div/div[1]/a/div[1]').click()

#coleta de dados com o Selenium - Web scraping com o Python
#envio de email avisando quando algo acontecer

#CONTINUAR ATRAVES DO VIDEO: https://www.youtube.com/watch?v=-LasZzyU9jI



















