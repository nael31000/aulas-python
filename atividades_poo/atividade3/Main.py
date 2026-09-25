from mamifero import Mamifero
from ave import Ave

leao = Mamifero(nome="Symba", idade=5, nivel_fome=70, velocidade_kmh=80)
gaviao = Ave(nome="Sky", idade=2, nivel_fome=75, envergadura_asas=120)

leao.__nivel_fome = -999
leao.__idade = -10

leao.correr()
gaviao.voar()
gaviao.voar()

leao.alimentar(50)
leao.alimentar(-10)

print("\n--- RESUMO DO MAMÍFERO ---")
leao.emitir_som()
leao.exibir_resumo()

print("\n--- RESUMO DA AVE ---")
gaviao.emitir_som()
gaviao.exibir_resumo()