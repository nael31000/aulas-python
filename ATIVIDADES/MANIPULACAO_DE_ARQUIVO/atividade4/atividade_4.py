
import json

loja = {
    "nomeLoja" : "TechStore",
    "produtos": [
        {
            "nome": "mouse",
            "preco": 50.00,
            "quantidade": 10
        },
        {
            "nome": "teclado",
            "preco": 100.00,
            "quantidade": 5
        },
        {
            "nome": "teclado mecânico",
            "preco": 200.00,
            "quantidade": 10
        }
    ]
}

with open('estoque.json', 'w', encoding='utf-8') as arquivo:

    json.dump(loja, arquivo, ensure_ascii=False, indent=4)


with open('estoque.json', 'r', encoding='utf-8') as arquivo:
    dados_lidos = json.load(arquivo)

    for produto in dados_lidos["produtos"]:
        print(f"O {produto['nome']} custa R$ {produto['preco']:.2f}")

with open('estoque.json', 'w', encoding='utf-8') as arquivo:
    dados_lidos["produtos"].append(
        {
            "nome": "monitor 4k",
            "preco": 500.00,
            "quantidade": 15
        }
    )

    for produto in dados_lidos["produtos"]:
        if produto["nome"] == "teclado":
            desconto = produto["preco"] * 0.9
            produto["preco"] = desconto

    json.dump(dados_lidos, arquivo, ensure_ascii=False, indent=4)

print("PREÇOS ATUALIZADOS")
for produto in dados_lidos["produtos"]:
    print(f"O {produto['nome']} agora custa R$ {produto['preco']:.2f}"
          f"\n Quantidade estoque: {produto['quantidade']}")