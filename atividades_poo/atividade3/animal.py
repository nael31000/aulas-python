class Animal:
    def __init__(self, nome: str, idade: int, nivel_fome: int):
        self.nome = nome
        self.idade = idade
        self.nivel_fome = nivel_fome

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, valor: str):
        self.__nome = valor

    @property
    def idade(self) -> int:
        return self.__idade

    @idade.setter
    def idade(self, valor: int):
        if valor < 0:
            print("Erro: Idade inválida")
        else:
            self.__idade = valor

    @property
    def nivel_fome(self) -> int:
        return self.__nivel_fome

    @nivel_fome.setter
    def nivel_fome(self, valor: int):
        if valor < 0:
            self.__nivel_fome = 0
        elif valor > 100:
            self.__nivel_fome = 100
        else:
            self.__nivel_fome = valor

    def alimentar(self, porcao: int):
        if porcao <= 0:
            print("Erro: Porção inválida")
        else:
            self.nivel_fome = self.nivel_fome - porcao

    def emitir_som(self):

        print(f"{self.nome} fazer uma som genérico.")

    def exibir_resumo(self):

        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade} anos")
        print(f"Nível de Fome: {self.nivel_fome}")