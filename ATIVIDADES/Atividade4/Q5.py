idade=int(input("Digite sua idade: "))
convite_vip = int(input("Você possui convite VIP? (1 para Sim, 0 para Não): "))
organizador = int(input("Você é organizadora do evento? (1 para Sim, 0 para Não): "))


if convite_vip == 1 and idade >= 18 or organizador == 1:
    print("Entrada PERMITIDA! Seja bem-vindo(a")
else:
    print("Entrada NEGADA! Você não atende aos requisitos")






