##Instruções: Resolva as questões abaixo aplicando o conceito de encapsulamento em Python para garantir a segurança dos dados e o cumprimento das regras de negócio.

#Questão 1: Sistema de Controle de Estoque (E-commerce)
#Você faz parte da equipe de back-end de um e-commerce. O sistema atual tem um problema grave: a classe Produto está com seus atributos públicos. Isso permitiu que scripts externos alterassem o preço dos produtos para valores negativos e realizassem vendas de itens sem estoque. Seu objetivo é refatorar a classe Produto aplicando Encapsulamento para blindar o sistema.

#O que você deve usar:
#Uma classe chamada Produto.
#Método construtor __init__ para inicializar o objeto.
#Atributos privados (utilizando o prefixo com dois underlines __): __nome, __preco e __quantidade_estoque.
#Métodos públicos de interação para encapsular a lógica e validar as alterações.

O seu sistema deve conter os seguintes métodos, respeitando rigorosamente estas validações:
adicionar_estoque(quantidade):
Regra: Só deve permitir adicionar valores maiores que zero ao estoque.
Resultado esperado: Se o valor for válido, o estoque aumenta. Se o usuário tentar adicionar um valor negativo ou zero, o sistema deve exibir a mensagem "Erro: Quantidade inválida" e o estoque não deve ser alterado.
realizar_venda(quantidade):
Regra: Só pode reduzir o estoque se a quantidade solicitada for menor ou igual ao estoque atual e maior que zero.
Resultado esperado: Se houver estoque suficiente, a venda é aprovada e o estoque reduzido. Caso a quantidade seja maior que o estoque, o sistema deve exibir "Venda negada: Estoque insuficiente" e bloquear a alteração.
aplicar_desconto(percentual):
Regra: O desconto não pode ser maior que 80% (política antifraude da empresa) e deve ser maior que 0%.
Resultado esperado: O preço do produto é recalculado com o desconto. Se o percentual for inválido, o sistema exibe "Erro: Desconto inválido" e o preço original se mantém intacto.
exibir_resumo():
Regra: Criação de um método auxiliar para visualizar o estado atual dos dados encapsulados.
Resultado esperado: Impressão na tela do nome do produto, seu preço atual e a quantidade em estoque para conferência.
OBS: pode usar o método __dict__ no final pra mostrar todas as informações reais do seu objeto


class Produto
    def __init__(self, nome, preco, quantidade_estoque):
        self.__nome = nome
        self.__preco = preco
        self.__quantidade_estoque = quantidade_estoque

    def adicionar_estoque(self, quantidade_estoque):
        if quantidade_estoque > 0:
            self.__quantidade_estoque += quantidade_estoque
        else:
            print("Erro: Quantidade inválida")

    def realizar_venda(self, quantidade_estoque):
        if quantidade