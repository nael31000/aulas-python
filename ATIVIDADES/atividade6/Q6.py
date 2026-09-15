# Crie um programa onde o computador "pensa" em um número secreto
# (você pode definir um número fixo diretamente no código, por exemplo, numero_secreto = 14).
# O usuário deve tentar adivinhar qual é esse número. Usando a estrutura while,
# o programa deve continuar pedindo um novo palpite enquanto o usuário não acertar.
# Requisito extra: Crie uma variável para contar quantas tentativas o usuário fez.
# Quando ele finalmente acertar o número, exiba a mensagem:
# "Parabéns! Você acertou o número secreto em [X] tentativas!" (onde X é o número de vezes que ele tentou).

numero_secreto = 14
tentativas= 1
numero_digitado=int(input("Diga um numero inteiro: "))

while numero_digitado != numero_secreto:
    print("Senha incorreta")
    numero_digitado=int(input("Diga um numero inteiro: "))
    tentativas += 1

print(f"Parabéns! Você acertou o número secreto em {tentativas} tentativas!")