from selenium import webdriver
from time import sleep

class ChromeAuto:
    def __init__(self):
        self.driver_path = 'chromedriver'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('user-data-dir-Perfil')
        self.chrome = webdriver.Chrome(
            self.driver_path,
            options=self.options
        )

    def clica_sign_in(self):
        try:
            btn_sign_in = self.chrome.find_element_by_link_text('Sign in') #pedi para selecionar o botao de sign in
            btn_sign_in.click() #pedi para clicar no botao de sign in
        except Exception as e:
            print('Erro ao clicar no botão Sign in', e)

    def acessa(self, site):
        self.chrome.get(site)

    def sair(self):
        self.chrome.quit()

    def faz_logout(self):
        try:
            perfil = self.chrome.find_element_by_css_selector('body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > details > details-menu > form > button')
            perfil.click()
        except Exception as e:
            print('Erro ao fazer logout: ', e)

    def verifica_usuario(self, usuario): #teste automatizado
        profile_link = self.chrome.find_element_by_css_selector('body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > details > details-menu > div.header-nav-current-user.css-truncate > a')
        profile_link_html = profile_link.get_attribute('innerHTML')
        assert usuario in profile_link_html

    def clica_perfil(self):
        try:
            perfil = self.chrome.find_element_by_css_selector('body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > details')
            perfil.click()
        except Exception as e:
            print('Erro ao clicar no Perfil: ', e)

    def faz_login(self):
        try:
            input_login = self.chrome.find_element_by_id('login_field')
            input_password = self.chrome.find_element_by_id('password')
            btn_login = self.chrome.find_element_by_name('commit')

            input_login.send_keys('r.cardoso.monteiro1@gmail.com')
            input_password.send_keys('@Yamato2645')
            sleep(3)
            btn_login.click()
        except Exception as e:
            print('Erro ao fazer login', e)

if __name__ == '__main__':
    chrome = ChromeAuto()
    chrome.acessa('https://github.com/')

    # chrome.clica_perfil()
    # chrome.faz_logout()

    chrome.clica_sign_in()
    chrome.faz_login()

    chrome.clica_perfil()
    chrome.verifica_usuario('renatamoon')

    sleep(5)
    chrome.sair()