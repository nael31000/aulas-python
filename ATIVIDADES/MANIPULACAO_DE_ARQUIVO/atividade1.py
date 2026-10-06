
usuario = input("Digite seu nome para iniciar a compra: ")


carrinho = []
total_compra = 0.0

while True:
    produto = input("Digite o nome do produto (ou 'fim' para encerrar): ")


    if produto.lower() == "fim":
        break

    try:
        preco = float(input(f"Digite o preço de '{produto}': R$ "))

        carrinho.append([produto, preco])
        total_compra += preco
    except ValueError:
        print("Preço inválido! Por favor, digite apenas números.")


print("\n--- FINALIZANDO COMPRA ---")
with open("pagamento.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(f"Cliente: {usuario}\n")
    arquivo.write("-" * 30 + "\n")
    arquivo.write("Itens do Carrinho:\n")

    for item in carrinho:

        arquivo.write(f"- {item[0]}: R$ {item[1]:.2f}\n")

    arquivo.write("-" * 30 + "\n")

    arquivo.write(f"TOTAL: R$ {total_compra:.2f}\n")


print("\n--- PROCESSANDO PAGAMENTO ---")
with open("pagamento.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()


    indice_total = conteudo.find("TOTAL: R$ ")

    if indice_total != -1:

        inicio_valor = indice_total + len("TOTAL: R$ ")


        fim_valor = conteudo.find("\n", inicio_valor)


        if fim_valor == -1:
            valor_extraido = conteudo[inicio_valor:]
        else:
            valor_extraido = conteudo[inicio_valor:fim_valor]


        print(f"Compra processada com sucesso! Valor cobrado: R$ {valor_extraido}")
    else:
        print("Erro: Total não encontrado no arquivo de pagamento.")