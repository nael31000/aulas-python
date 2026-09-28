class ItemPedido:

    def __init__(self, descricao, valor):
        self.descricao = descricao

        try:
            self.valor = float(valor)
        except ValueError:
            raise ValueError(
                f"Erro: O valor para '{self.descricao}' deve ser estritamente numérico."
            ) from None
        except TypeError:
            raise ValueError(
                f"Erro: O valor para '{self.descricao}' deve ser estritamente numérico."
            ) from None


class Mesa:


    def __init__(self, numero_mesa):
        self.numero_mesa = numero_mesa
        self.pedidos = []

    def adicionar_pedido(self, item):


        if not isinstance(item, ItemPedido):
            raise TypeError("O objeto informado deve ser do tipo ItemPedido.")

        self.pedidos.append(item)
        print(f"-> {item.descricao} adicionado à {self.numero_mesa}.")

    def somar_total(self):


        return float(sum(pedido.valor for pedido in self.pedidos))

    def fechar_conta(self, taxa_servico):


        try:
            taxa_percentual = float(taxa_servico)
        except ValueError:
            raise ValueError(
                "Erro: A taxa de serviço deve ser um valor numérico."
            ) from None
        except TypeError:
            raise ValueError(
                "Erro: A taxa de serviço deve ser um valor numérico."
            ) from None

        if taxa_percentual < 0:
            raise ValueError("Erro: A taxa de serviço não pode ser negativa.")

        subtotal = self.somar_total()
        valor_servico = subtotal * (taxa_percentual / 100)
        total_final = subtotal + valor_servico

        print(f"\n--- EXTRATO DA {self.numero_mesa} ---")

        if self.pedidos:
            for pedido in self.pedidos:
                print(f"{pedido.descricao}: R$ {pedido.valor:.2f}")
        else:
            print("Nenhum pedido registrado.")

        print(f"Subtotal: R$ {subtotal:.2f}")
        print(f"Taxa de serviço ({taxa_percentual:g}%): R$ {valor_servico:.2f}")
        print(f"Total a pagar: R$ {total_final:.2f}")
        print("-" * 45)

        self.pedidos.clear()


def registrar_pedido_seguro(mesa, descricao, valor):
    try:
        item = ItemPedido(descricao, valor)
        mesa.adicionar_pedido(item)
    except ValueError as erro:
        print(f"ALERTA DO SISTEMA: {erro}")



mesa1 = Mesa("Mesa 1")


registrar_pedido_seguro(mesa1, "Pizza Margherita", 45.90)
registrar_pedido_seguro(mesa1, "Refrigerante", 8.50)


print("\n--- TESTANDO ENTRADA INVÁLIDA ---")
registrar_pedido_seguro(mesa1, "Pudim", "quinze")
registrar_pedido_seguro(mesa1, "Café", "5,50")

registrar_pedido_seguro(mesa1, "Suco de Laranja", 12.00)

print("\n--- FECHAMENTO DA CONTA ---")
mesa1.fechar_conta(taxa_servico=10)

print("\n--- VERIFICANDO STATUS DA MESA APÓS FECHAMENTO ---")
mesa1.fechar_conta(taxa_servico=10)