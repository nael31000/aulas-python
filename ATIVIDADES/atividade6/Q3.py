#Faça um programa que peça ao usuário para digitar números inteiros repetidamente.
# O programa deve continuar pedindo números até que o usuário digite o número 0 (zero).
# Quando o usuário digitar 0, o laço deve ser encerrado e o programa deve exibir a soma de todos os números que
# foram digitados até aquele momento.

numero = int(input("Digite um numero inteiro: "))
contagem = 0
while numero!= 0:
    contagem += numero
    numero= int(input("Digite um numero novamente: "))

print("a soma de todos os números foi",contagem)