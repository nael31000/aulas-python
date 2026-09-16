class Carro:
    def __init__(self, cor,, tipo, modelo, ano, fabricante):  new
        self.cor = cor
        self.tip= tipo
        self.modelo = modelo
        self.ano = ano
        self.fabricante = fabricante
    def __str__(self): new
        return f"Valores do objeto {self.cor,self.tipo, self.modelo}:"