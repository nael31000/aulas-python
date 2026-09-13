# Imagine que você tem um orçamento total para uma viagem, por exemplo, R$ 500.
# Escreva um programa que defina esse valor em uma variável
# e peça ao usuário para digitar o valor de cada gasto que ele realizar.
# Usando um laço while, o programa deve subtrair cada gasto do orçamento total e exibir o saldo restante.
# O laço deve continuar pedindo novos gastos enquanto o orçamento for maior que zero.
# Se o usuário gastar todo o dinheiro (ou seja, o orçamento chegar a zero ou ficar negativo),
# o programa deve encerrar o laço e exibir a mensagem:\
# "Atenção: Você ficou sem saldo ou estourou seu orçamento!"

orcamento = 500
gasto=0

while orcamento > 0:
    gasto = float(input("Digite o valor de gasto: "))
    orcamento -= gasto
    print(f"saldo restante R$ {orcamento}")


print("Atenção: Você ficou sem saldo ou estourou seu orçamento")

