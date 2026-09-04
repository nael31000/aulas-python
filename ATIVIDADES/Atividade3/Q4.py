#Construa um sistema escolar que leia a Nota 1 e a Nota 2 de um aluno,
# além da sua Porcentagem de Frequência. O programa deve primeiro calcular a média das notas.
# Para o aluno ser aprovado, ele precisa de duas coisas ao mesmo tempo: uma média maior ou igual a 6.0
# E uma frequência maior ou igual a 75. Exiba a média calculada e, em seguida, exiba True se ele foi
# aprovado ou False se reprovou, usando o operador and.

Nota1=float(input("qual a primeira nota"))
Nota2=float(input("qual a segunda nota"))
Frequencia=int(input("qual a frequencia"))
media=(Nota1+Nota2)/2

aceito=media>= 6.0 and Frequencia>=75
print(aceito)