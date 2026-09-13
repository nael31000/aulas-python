# Faça um programa que peça ao usuário para digitar números inteiros repetidamente.
# O programa deve continuar pedindo números até que o usuário digite o número 0 (zero).
# Quando o usuário digitar 0, o laço deve ser encerrado
# e o programa deve exibir a soma de todos os números que foram digitados até aquele momento.

soma_total=0
numero = int(input("digite um numero inteiro: "))

while numero != 0:
    soma_total+=numero
    numero=int(input("digite um numero inteiro: "))

print("final", soma_total)