# Crie um programa que mostre repetidamente um menu com duas opções:
# 1 - Mostrar saudação
# 2 - Sair do programa
# O programa deve pedir para o usuário escolher uma opção. Usando while:
# Se ele digitar 1, exiba "Olá, seja muito bem-vindo(a)!".
# Se ele digitar qualquer número diferente de 1 e 2, exiba "Opção inválida!".
# O programa só deve parar de repetir e encerrar quando o usuário digitar 2,
# exibindo a mensagem "Programa encerrado."



pedido=0

while pedido!=2:
    print("1-mostrar saudacao e 2- sair do programa")
    pedido=int(input("digite sua opcao: "))
    if pedido==1:
        print("mostrar saudacoa")
    elif pedido==2:
        print("sair do programa")
    else:
        print("opcao invalida")
