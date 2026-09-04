#resposta Q1
#Crie um programa para um restaurante que funciona como uma calculadora de divisão de conta.
# O sistema deve solicitar ao usuário o valor total da conta (ex: 150.00) e a quantidade de pessoas na mesa.
# O programa deve calcular o valor que cada um deve pagar e exibir a mensagem:
# "O valor total foi de R$ [Total], e cada pessoa deve pagar R$ [Valor Dividido]".
conta=(float(input("qual eho valor da conta")))
Quantidade=(int(input("qual eh a quantidade de pessoas na mesa")))
div=conta/Quantidade
print(f"o valor total foi de R$ {conta} e cada pessoa deve pagar R${div:.2f}")
