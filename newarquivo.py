#estudos

#muitos valores para multiplas variáveis

from typing import overload


x, y, z = "Laranja", "Banana", "Pessego"

print(x)
print(y)
print(z)

#muitos valores para multiplas variáveis

x = y = z = "Orange"
print(x)
print(y)
print(z)

#listas

frutas = ["maça", "banana", "pessego"]
x, y, z = frutas

print(x)
print(y)
print(z)

#saida de variáveis

x = "otimo"
print("Python é " + x)

x = "Python is "
y = "awesome"
z =  x + y
print(z)

#criando uma variável fora de uma função e usar isso dentro
#uma função

x = "otimo"

def myfunc():
    print("Python é " + x)

myfunc()

print("Python é " + x)

def myfunc():
    global x
    x = "fantastico"
myfunc()

print("Python é " + x)

#exercicio - Crie uma variável nome da NOME DO CARRO e
#assimile ao valor de volvo

carname = str("Volvo")
print(carname)


