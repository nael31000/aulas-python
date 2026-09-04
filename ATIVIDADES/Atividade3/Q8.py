nome_produto = input("Digite o nome do produto: ")
custo = float(input("Digite o custo de fábrica: R$ "))
preco_venda = float(input("Digite o preço de venda: R$ "))

lucro = preco_venda - custo
lucro_bom = lucro > 20

print("Produto:", nome_produto)
print("Lucro obtido: R$", lucro)
print("Lucro foi bom?", lucro_bom)
