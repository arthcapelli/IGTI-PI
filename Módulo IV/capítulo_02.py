# -*- coding: utf-8 -*-
"""Capítulo_02.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wMsaJBRTPGl9Jbv9akJ81wWVLilJY8qH
"""

nome = input("Insira seu nome: ")
if "José" in nome:
  print("Vc tem José no nome!")
else:
  print("Vc não tem José no nome!")

nome = input("Insira seu nome: ")
if len(nome) > 20:
  print("O nome deve ter no máximo 20 caracteres!")
print("Nome digitado: {}".format(nome))

usuario = input("Digite o usuário: ")
senha = input("Digite a senha: ")
if (usuario == "marcelo") and (senha == "secreto"):
  print("Parabéns, vc tem acesso ao sistema!")
else:
  print("Usuário ou senha inválidos!")

# Tem carteira de moto
# Tem carteira de carro
# Se tiver carteira de carro então seu nível = 1
# Se tiver carteira de moto então seu nível = 2
# Se tiver carteira de carro E de moto então seu nível = 3
# Algoritmo para calcular o nível do funcionário
questao = input("Vc tem carteira de moto (S/N)? ")
carteira_moto = (questao.upper()=="S") or (questao.upper()=="SIM")
questao = input("Vc tem carteira de carro (S/N)? ")
carteira_carro = (questao.upper()=="S") or (questao.upper()=="SIM")

if (carteira_carro) and (not(carteira_moto)):
  print("Vc está no nível 1!")
elif (not(carteira_carro)) and (carteira_moto):
  print("Vc está no nível 2!")
elif (carteira_carro) and (carteira_moto):
  print("Vc está no nível 3!")

# primeiro emprego?
# tem alguma carteira?
# só pode trabalhar na empresa SE for primeiro emprego OU tiver habilitação
questao = input("É o seu primeiro emprego (S/N)? ")
primeiro_emprego = (questao.upper()=="S") or (questao.upper()=="SIM")
questao = input("Vc tem habilitação (S/N)? ")
habilitacao = (questao.upper()=="S") or (questao.upper()=="SIM")

if (primeiro_emprego) or (habilitacao):
  print("Vc pode trabalhar na nossa empresa!")
else:
  print("Desculpe, não há vagas para vc!")

# Jogo de dados
# Escolha o valor entre 1 e 6
# Escolha quanto quer apostar (valor máx 100)
# Joga 2 dados
# Se der 1 dado igual, ganha 2x o valor apostado
# Se der 2 dados iguais, ganha 10x o valor apostado
# Se não der nenhum dado igual, perde o dinheiro
from random import randrange

bolso = 100
numero_apostado = int(input("Em qual número vc aposta? "))
if (numero_apostado > 6) or (numero_apostado < 1):
  print("Vc apostou em um número inválido!")
else:
  valor_aposta = float(input("Qual é o valor da aposta? "))
  if valor_aposta > bolso:
    print("Vc não tem esse dinheiro!")
  else:
    bolso = bolso - valor_aposta
    dado1 = randrange(1,6)
    dado2 = randrange(1,6)
    mensagem_ganho = "Vc ganhou R${} e agora está com R${}!"
    print("Sorteados os dados {} e {}.".format(dado1, dado2))

    resultado = 0
    if (dado1 == numero_apostado) and (dado2 == numero_apostado):
      resultado = valor_aposta*10
      bolso = bolso + resultado
      print(mensagem_ganho.format(resultado, bolso))
    elif (dado1 == numero_apostado) or (dado2 == numero_apostado):
      resultado = valor_aposta*2
      bolso = bolso + resultado
      print(mensagem_ganho.format(resultado, bolso))
    else:
      print("Vc errou. Agora tem no bolso R${}.".format(bolso))

# Cálculo IMC
# peso/(altura**2)
# menor que 17 = mt abaixo
# entre 17 e 18.5 = abaixo do peso
# entre 18.5 e 25 = peso normal
# entre 25 e 30 = acima do peso
# entre 30 e 35 = obesidade grau I
# entre 35 e 40 = obesidade grau II
# acima de 40 = obesidade mórbida

print("Olá, vamos ajudar vc a ficar saudável! Primeiro precisamos saber seu IMC.")

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso/(altura**2)
print("Seu IMC é {}.".format(imc))

if imc < 17:
  print("Vc está mt abaixo do peso!")
elif (imc >= 17) and (imc < 18.5):
  print("Vc está abaixo do peso!")
elif (imc >= 18.5) and (imc < 25):
  print("Vc está com peso normal!")
elif (imc >= 25) and (imc < 30):
  print("Vc está acima do peso!")
elif (imc >= 30) and (imc < 35):
  print("Vc está com obesidade grau I!")
elif (imc >= 35) and (imc < 40):
  print("Vc está com obesidade grau II!")
elif (imc > 40):
  print("Vc está com obesidade mórbida!")

