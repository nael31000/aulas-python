idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso em kg: "))

pode_doar = idade >= 16 and idade <= 69 and peso > 50

print(pode_doar)
