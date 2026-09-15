#Escreva um programa que defina uma senha fixa no código (por exemplo, "123456").
# Peça para o usuário digitar a senha. Enquanto a senha digitada não for igual à senha correta,
# exiba a mensagem: "Senha incorreta. Tente novamente." e peça a senha de novo (igual ao exemplo do "Joao" visto em aula).
# Quando o usuário acertar, exiba: "Acesso permitido!".

#senha=123
#123
# senha_digitada=int(input("Digite sua senha: "))


senha_correta = "123456"
senha = input("Digite a senha: ")

while senha != senha_correta:
    print("Senha incorreta. Tente novamente.")
    senha = input("Digite a senha: ")

print("Acesso permitido!")
