#Simulador de dados - PROJETO 1 - simulação de um dados gerando
#um valor de 1 até 6
#Renata Monteiro

import random

class SimuladorDeDado:

    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = "Gerar um novo valor para o dado? "
    #funcionalidade inicial do python
    def Iniciar(self):
        resposta = input(self.mensagem) #retornar a mensagem gerar um
        #novo valor de dados
        try: #somente para tratar
            if resposta == 'sim' or resposta == 's':
                self.GerarValorDoDado()
            elif resposta == 'não' or resposta == 'n':
        #tratando das possibilidades dods erros da resposta do
        #usuário
                print('Obrigada por participar')
            else:
                print('Favor digitar sim ou não')
        except:
            print('ERRO AO RECEBER SUA RESPOSTA')


    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo,self.valor_maximo))
         #gerar o valor minimo e um valor maximo inteiro

simulador = SimuladorDeDado()
simulador.Iniciar() #inciando o simulador
