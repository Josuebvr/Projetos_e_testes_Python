import string
from random import random, choice
valores = string.ascii_letters + string.digits + string.punctuation
tamanho = 15
senha = ''
for i in range(tamanho):
    senha += choice(valores)
print(senha)


# string.ascii_letters (todas as letras)
# string.digits (numeros de 0 a 9)
# string.punctuation (caracteres especiais)
