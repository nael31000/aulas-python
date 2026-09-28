from abc import ABC, abstractmethod

class Frete(ABC):

    def __init__(self, distancia_km: float, peso_kg: float):
        self._distancia_km = distancia_km
        self._peso_kg = peso_kg

    def iniciar_processo(self):
        print("Sistema central: oeração de frete iniciada.")

    def obter_dados(self):
        return self._distancia_km, self._peso_kg

    @abstractmethod
    def calcular(self, distancia_km: float, peso_kg: float) -> float:
        pass



class Caminhao(Frete):

    def calcular(self, distancia_km: float, peso_kg: float) -> float:
        if distancia_km <= 0:
            print("Caminhão: distânca inválida.")
            return 0.0

        if peso_kg > 5000:
            print("Caminhão: carga acima de 5000 kg. Frete no permitido.")
            return 0.0

        custo = (distancia_km * 5.00) + (peso_kg * 0.10)

        print(
            f"Caminhão: frte calculado = R$ {custo:.2f} "
            f"para {distancia_km} km e {peso_kg} kg."
        )

        return custo


class Navio(Frete):

    def calcular(self, distancia_km: float, peso_kg: float) -> float:
        if distancia_km <= 0:
            print("Navio: distância inválida.")
            return 0.0

        if peso_kg <= 0:
            print("Navi: peso inválido.")
            return 0.0

        custo = 1000.00 + (distancia_km * 0.80) + (peso_kg * 0.01)

        print(
            f"Navio: frete calculado = R$ {custo:.2f} "
            f"para {distancia_km} km e {peso_kg} kg."
        )

        return custo


class Drone(Frete):

    def calcular(self, distancia_km: float, peso_kg: float) -> float:
        if distancia_km <= 0:
            print("Drone: distância inválida.")
            return 0.0

        if peso_kg > 2:
            print("Drome: envio recusado, pois a carga é maior que 2 kg.")
            return 0.0
        else:
            custo = (distancia_km * 20.00) + (peso_kg * 5.00)

            print(
                f"Drone: frete calculado = R$ {custo:.2f} "
                f"para {distancia_km} km e {peso_kg} kg."
            )

            return custo



def processar_lote(lista_de_objetos):

    for item in lista_de_objetos:
        item.iniciar_processo()

        distancia_km, peso_kg = item.obter_dados()

        item.calcular(distancia_km, peso_kg)

        print("-" * 30)



if __name__ == "__main__":

    obj1 = Caminhao(200, 1200)
    obj2 = Navio(800, 50000)
    obj3 = Drone(15, 1.8)
    obj4 = Drone(10, 3.5)  # Este deve ser recusado por causa do peso

    lote = [obj1, obj2, obj3, obj4, obj1]  # Pode repetir tipos

    print("\n--- INICANDO PROCESSAMENTO EM LOTE ---")
    processar_lote(lote)

    print("\n--- ROTEIRO DE TESTE COM FOR EXPLÍCITO ---")

    for item in lote:
        item.iniciar_processo()

        distancia_km, peso_kg = item.obter_dados()

        item.calcular(distancia_km, peso_kg)

        print("-" * 30)


