#Uma fábrica empacota maçãs em caixas que cabem exatamente 12 unidades.
# Crie um programa que pergunte ao usuário a quantidade total de maçãs colhidas no dia.
# Utilizando o operador de módulo (%), calcule e exiba na tela quantas maçãs sobrarão fora das caixas
# (ou seja, o resto da divisão por 12).

quantidade=float(input("Quantas macas colhidas"))
sobras=quantidade%12
print("sobraras", sobras,"macas")