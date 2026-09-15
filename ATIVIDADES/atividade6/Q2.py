# Escreva um programa que defina uma senha fixa no código (por exemplo, "123456").
# Peça para o usuário digitar a senha. Enquanto a senha digitada não for igual à senha correta,
# exiba a mensagem: "Senha incorreta. Tente novamente."
# e peça a senha de novo (igual ao exemplo do "Joao" visto em aula).
# Quando o usuário acertar, exiba: "Acesso permitido!".

senha=123456
senha_digitada=int(input("Diga sua senha: "))

while senha_digitada != senha:
    print("Senha incorreta")
    senha_digitada = int(input("Diga sua senha: "))

print("Acesso Permitido")