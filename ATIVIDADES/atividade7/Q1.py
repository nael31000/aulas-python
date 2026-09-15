# Crie uma lista que ela armazene um numero x de funcionários. Usando o while,
# adicione quantos funcionários quiser em execução (input).
#
# Com o for, você irá imprimir duas listas:
# Uma lista com todos os funcionários que receberão um aumento.
# Outra lista, com todos os funcionário que serão demitidos.
#
# Você irá decidir qual funcionário será demitido ou receberá aumento pelo index do funcionário lista[]

lista_funcionarios = []

while True:
    lista_funcionarios.append(input("Digite o nome do funcionario: "))
    opcao = input("Digite 1 para continuar, 2 para sair: ")
    if opcao != "1":
        print(f"Todos os funcionários: {lista_funcionarios}")
        print("Quantidade de funcionários:", len(lista_funcionarios))
        break

lista_demitidos = []
lista_aumento = []

print("\nLista de TODOS os funcionários:")
for index in range(len(lista_funcionarios)):
    print(f"Funcionário {index}: {lista_funcionarios[index]}")

repeticao = 0
for index in range(len(lista_funcionarios)):
    repeticao += 1
    if repeticao % 2 == 0:
        lista_demitidos.append(lista_funcionarios[index])
    else:
        lista_aumento.append(lista_funcionarios[index])

print("\nLista dos funcionários DEMITIDOS:")
print(lista_demitidos)

print("\nLista dos funcionários AUMENTO:")
print(lista_aumento)

lista_numeros = [10, 9, 6, 7]
print("\nMaior número:", max(lista_numeros))
print("Menor número:", min(lista_numeros))

media = sum(lista_numeros) / len(lista_numeros)
print("Média das suas notas:", media)