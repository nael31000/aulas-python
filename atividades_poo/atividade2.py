class Produto:
    def __init__(self, nome, preco, quantidade_estoque):
        self.__nome = nome
        self.__preco = preco
        self.__quantidade_estoque = quantidade_estoque

    def adicionar_estoque(self, quantidade):
        if quantidade > 0:
            self.__quantidade_estoque += quantidade
            print(f"Estoque atualizado. Novo total: {self.__quantidade_estoque} unidades.")
        else:
            print("Erro: Quantidade inválida")

    def realizar_venda(self, quantidade):
        if quantidade <= 0:
            print("Erro: Quantidade inválida")
        elif quantidade <= self.__quantidade_estoque:
            self.__quantidade_estoque -= quantidade
            print(f"Venda de {quantidade} unidades aprovada. Estoque restante: {self.__quantidade_estoque}.")
        else:
            print("Venda negada: Estoque insuficiente")

    def aplicar_desconto(self, percentual):
        if 0 < percentual <= 80:
            self.__preco = self.__preco * (1 - percentual / 100)
            print(f"Desconto de {percentual}% aplicado. Novo preço: R$ {self.__preco:.2f}")
        else:
            print("Erro: Desconto inválido")

    def exibir_resumo(self):

        print("\n--- Resumo do Produto ---")
        print(f"Nome: {self.__nome}")
        print(f"Preço: R$ {self.__preco:.2f}")
        print(f"Estoque: {self.__quantidade_estoque} unidades")
        print("-------------------------\n")



# TESTES
print(">> Instanciando o produto de teste...")
meu_produto = Produto("Notebook Gamer", 5000.00, 10)
meu_produto.exibir_resumo()

print(">> 1. Tentando forçar a alteração direta dos atributos (Ataque malicioso)...")
meu_produto.__quantidade_estoque = -50
meu_produto.__preco = -100
print("Tentativa de alteração direta executada.\n")

print(">> 2. Tentando realizar uma venda absurdamente maior que o estoque...")
meu_produto.realizar_venda(9999)

print("\n>> 3. Exibindo o resumo final (Comprovando que os dados reais não foram afetados)...")
meu_produto.exibir_resumo()

print(">> 4. Exibindo todas as informações reais do objeto com __dict__...")
print(meu_produto.__dict__)