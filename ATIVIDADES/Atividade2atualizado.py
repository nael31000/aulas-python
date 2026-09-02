#resposta
nome = input("Qual é o seu nome? ")
idade = int(input("Qual é sua idade? "))
plano_de_saude = input("Tem plano de saúde (True ou False)? ")

aceito = idade >= 18 and idade <= 65 and plano_de_saude == "True"
print("Seu nome é", nome, "você tem", idade, "anos. Tem plano?", plano_de_saude, "Você foi aceito?", aceito)
