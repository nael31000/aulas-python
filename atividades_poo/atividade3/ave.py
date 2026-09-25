from animal import Animal

class Ave(Animal):
    def __init__(self, nome: str, idade: int, nivel_fome: int, envergadura_asas: float):
        super().__init__(nome, idade, nivel_fome)
        self.envergadura_asas = envergadura_asas

    @property
    def envergadura_asas(self) -> float:
        return self.__envergadura_asas

    @envergadura_asas.setter
    def envergadura_asas(self, valor: float):
        self.__envergadura_asas = valor

    def voar(self):
        if self.nivel_fome <= 80:
            print(f"{self.nome} voou com suas asas de {self.envergadura_asas}cm!")
            self.nivel_fome = self.nivel_fome + 15
        else:
            print(f"Voo negado: {self.nome} está faminto demais para voar!")

    def emitir_som(self):
        print(f"{self.nome} canta um som melodioso!")

    def exibir_resumo(self):
        super().exibir_resumo()
        print(f"Envergadura das asas: {self.envergadura_asas} cm")
