
#a senha digitada esta como texto e deve ser um int
senha_cadastrada = 1234
senha_digitada = int(input("Digite sua senha: "))

acesso_liberado = senha_cadastrada == senha_digitada

print("Acesso liberado?", acesso_liberado)
