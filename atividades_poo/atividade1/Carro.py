#Crie uma classe que tenha no mínimo 5 atributos, 1 construtor, 3 métodos convencionais.

#Sua classe deve ser uma das opções abaixo:
#CARRO
   #Banco
   # Pessoa

#Você escolhe quais atributos relacionar com o conceito da sua classe.

#No final, quero 5 objetos diferentes instanciados, e seu programa deve exibir em uma lista FORA da classe todos os seus objetos.


############################################################################
class Carro:
    def __init__(self, cor, dono, tipo, modelo, ano, fabricante):
        self.cor = cor
        self.dono = dono
        self.tipo = tipo
        self.modelo = modelo
        self.ano = ano
        self.fabricante = fabricante

    def __str__(self):
        return (f"Informações do carro:\n"
                f"\tCor: {self.cor}\n"
                f"\tDono: {self.dono}\n"
                f"\tTipo: {self.tipo}\n"
                f"\tModelo: {self.modelo}\n"
                f"\tAno: {self.ano}\n"
                f"\tFabricante: {self.fabricante}")

    def abastecer(self):
        print(f"O {self.dono} abasteceu o {self.modelo}!")

    def deslocar (self):
        print(f"O {self.modelo} de {self.dono} deslocou.")

    def virar (self):
        print(f"a {self.modelo} de {self.dono} virou")



carro1 = Carro(cor="Vermelho", dono="João", tipo="Popular", modelo="Fiesta", ano="2016", fabricante="Ford")
carro2 = Carro(cor="Preto", dono="Maria", tipo="SUV", modelo="Tracker", ano="2022", fabricante="Chevrolet")
carro3 = Carro(cor="Branco", dono="Carlos", tipo="Sedan", modelo="Civic", ano="2020", fabricante="Honda")
carro4 = Carro(cor="Prata", dono="Ana", tipo="Hatch", modelo="Polo", ano="2019", fabricante="Volkswagen")
carro5 = Carro(cor="Azul", dono="Pedro", tipo="Picape", modelo="Hilux", ano="2023", fabricante="Toyota")

lista_carros = [carro1, carro2, carro3, carro4, carro5]

print("--- LISTA DE CARROS ---")
for carro in lista_carros:
    print(carro)

print("\n--- TESTANDO OS MÉTODOS ---")
carro1.abastecer()
carro3.deslocar()
carro5.virar()