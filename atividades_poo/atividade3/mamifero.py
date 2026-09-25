from animal import Animal

class Mamifero(Animal):
    def __init__(self, nome: str, idade: int, nivel_fome: int, velocidade_kmh: float):
        super().__init__(nome, idade, nivel_fome)
        self.velocidade_kmh = velocidade_kmh

    @property
    def velocidade_kmh(self) -> float:
        return self.__velocidade_kmh

    @velocidade_kmh.setter
    def velocidade_kmh(self, valor: float):
        self.__velocidade_kmh = valor

    def correr(self):
        print(f"{self.nome} correu a {self.velocidade_kmh} km/h!")
        self.nivel_fome = self.nivel_fome + 20

    def emitir_som(self):
        print(f"{self.nome} ruge/ruge alto!")

    def exibir_resumo(self):
        super().exibir_resumo()
        print(f"Velocidade: {self.velocidade_kmh} km/h")