import pandas as pd

df = pd.read_csv("funcionarios.csv", sep=';')

df_filtrado1 = df[df['salario']<3000]
print("salarios menores que R$ 3000: \n", df_filtrado1.salario)


df_filtrado2 = df[df['salario']>5000]
print("salarios superiores a R$ 5000: \n", df_filtrado2.salario)

df_filtrado3 = df[df['salario']==3100]
print("salario igual a R$ 3100: \n", df_filtrado3.salario)

df_filtrado_cargos = df[
    (df['cargo'] == "Analista de Dados")|
    (df['cargo'] == "Analista de Sistemas")|
    (df["cargo"] == "Desenvolvedor Java")|
    (df["cargo"] == "Cientista de Dados")
]
print("cargos filtrados")
print(df_filtrado_cargos)

df_filtrado4 = df[df["salario"]>6000][[ 'nome','cargo']]
print("\n\n\nFuncionários com salário acima de 6000:\n\n\n")
print(df_filtrado4)

df_id_pares= df[df['id'] % 2 ==0]

print("Funcionarios com ID PAR\n\n")
print(df_id_pares)