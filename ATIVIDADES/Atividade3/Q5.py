#Uma loja está em promoção: o cliente ganha frete grátis se o valor da compra for maior que R$ 200.00
# OU se ele possuir o cartão VIP da loja. Peça ao usuário o valor da compra e pergunte se ele é VIP
# (peça para digitar 1 para "Sim, sou VIP" ou 0 para "Não sou VIP").
# Crie a lógica usando o operador or e imprima True se ele tem direito ao frete grátis ou False caso não tenha.

valor = float(input("Digite o valor da compra"))
vip = int(input("Você é VIP? Digite 1 para Sim ou 0 para Não: "))

frete_gratis = valor > 200 or vip == 1

print(frete_gratis)
