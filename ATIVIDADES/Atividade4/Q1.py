#Crie um programa que peça ao usuário para digitar um número inteiro.
# O sistema deve verificar se o número é par ou ímpar utilizando o operador de resto da divisão (%).
# Se o resto da divisão por 2 for igual a zero, exiba na tela: "O número X é PAR".
# Caso contrário (else), exiba: "O número X é ÍMPAR".

numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    print("O número", numero, "é PAR")
else:
    print("O número", numero, "é ÍMPAR")