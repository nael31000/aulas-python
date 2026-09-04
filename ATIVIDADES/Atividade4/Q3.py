#Crie um programa que pergunte a idade do usuário. No Brasil, o voto é obrigatório para quem tem 18 anos ou mais.
# Escreva uma estrutura condicional onde, se a idade for maior ou igual a 18, o terminal imprima: "Você é obrigado a votar".
# Caso contrário, imprima: "Você ainda não é obrigado a votar".

idade = int(input("Digite sua idade: "))
if idade>=18:
    print("Você é obrigado a votar")
else:
    print("Você ainda não é obrigado a votar")
