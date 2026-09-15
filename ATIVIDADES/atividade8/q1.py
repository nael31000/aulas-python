#Crie uma única função que receba como parâmetro o nome de um aluno,
#sua nota do primeiro, segundo, terceiro e quarto bimestre.
#Sua função deve calcular a média final desse aluno, e imprimir na tela todos os valores,
#e informar se o aluno foi reprovado ou aprovado pela média final.

#OBS: valor da media = 7


def calcular_boletim(nome, nota1, nota2, nota3, nota4):
    media = (nota1 + nota2 + nota3 + nota4) / 4

    print(f"\n--- BOLETIM DO ALUNO ---")
    print(f"Nome: {nome}")
    print(f"Notas: {nota1}, {nota2}, {nota3}, {nota4}")
    print(f"Média Final: {media}")

    if media >= 7:
        print("Aprovado!")
    else:
        print("Reprovado.")


nome_aluno = input("Qual o nome do aluno? ")
n1 = float(input("Qual a primeira nota? "))
n2 = float(input("Qual a segunda nota? "))
n3 = float(input("Qual a terceira nota? "))
n4 = float(input("Qual a quarta nota? "))

calcular_boletim(nome_aluno, n1, n2, n3, n4)
