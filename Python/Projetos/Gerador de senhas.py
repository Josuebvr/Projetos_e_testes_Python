import random
letras_minusculas = "abcdefghijklmnopqrstuvwxyz"
letras_maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeros = "0123456789"
simbolos = "!@#$%&*()"
para_senha = letras_minusculas + letras_maiusculas + numeros + simbolos
tamanho_da_senha = 12
senha = "".join(random.sample(para_senha, tamanho_da_senha))
print("Minha senha: ", senha)