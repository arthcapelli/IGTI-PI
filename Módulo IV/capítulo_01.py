# -*- coding: utf-8 -*-
"""Capítulo_01.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1scKTU_bMt30uauz-t1sq9frcXDNd_Bde
"""

nome = "Arthur, de idade: {}, tem {} quilos."
idade = 26
peso = 58
print(nome.format(idade, peso))

#Esse programa mostra o nome de uma pessoa conforme o passaporte.

primeiro_nome = input("Digite o seu primeiro nome: ")
sobrenome = input("Digite o seu sobrenome: ")
print("O nome conforme o passaporte é: {}, {}.".format(sobrenome, primeiro_nome))

nome = input("Digite o primeiro nome: ")
sobrenome = input("Digite o segundo nome: ")
nome = nome.capitalize()
sobrenome = sobrenome.capitalize()
print("Nome: {} -- Sobrenome: {}".format(nome, sobrenome))

nome = "Marcelo Sampaio"
print(len(nome))
nome_dividido = nome.split()
print(nome_dividido)
print("Primeiro nome: {}".format(nome_dividido[0]))

nome = "Joaquim José da Silva Xavier"
nome = nome[-6:]
print(nome)

nome = input("Digite o seu nome: ")
print("Infelizmente só posso gravar 20 letras. Será gravado {}.".format(nome[0:20]))
primeiro_espaco = nome.index(" ")
primeiro_nome = nome[0:primeiro_espaco]
print("O primeiro nome é {}.".format(primeiro_nome))

frase = "----Esta é uma frase de testes   "
frase = frase.strip("-").strip()

print("*{}*".format(frase))

peso = input("Digite seu peso: ")
peso_dividido = peso.split(".")
print(peso_dividido[0].isdigit())
print(peso_dividido[1].isdigit())

idade = 18
print(idade)
peso = 80.9
print(peso)

preco_arroz = 4.99
quilos = 10
print(type(preco_arroz))
print(type(quilos))
print(preco_arroz * quilos)

# Programa para calcular o IMC - Índice de Massa Corporal
# Peso/(altura**2)
# input sempre "entrega" uma String, tem que passar para INT ou FLOAT

peso = float(input("Insira seu peso:"))
altura = float(input("Insira sua altura:"))
print(type(peso))
print(type(altura))
imc = peso/(altura**2)
print("O seu IMC é: {}".format(imc))