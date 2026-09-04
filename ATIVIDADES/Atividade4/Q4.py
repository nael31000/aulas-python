#Desenvolva um algoritmo que simule um saque bancário.
# O programa deve receber o saldo atual do cliente (ex: 500.00) e o valor que ele deseja sacar.
# Se o valor do saque for menor ou igual ao saldo disponível, o programa deve subtrair o valor sacado,
# atualizar o saldo e exibir: "Saque realizado com sucesso! Saldo atual: R$ [Novo Saldo]".
# Caso o saque seja maior que o saldo, exiba: "Saldo insuficiente para realizar esta operação".

saldo=float(input("Qual o seu saldo?"))
saque=float(input("Qual o valor do seu saque?"))
saldo_atual= saldo-saque
if saldo>=saque:
    print( "saque realizado com sucesso! saldo atual:", saldo_atual)
else:
    print("Saldo insuficiente para realizar esta operação")