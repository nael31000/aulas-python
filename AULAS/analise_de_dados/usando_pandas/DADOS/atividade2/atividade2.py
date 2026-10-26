import pandas as pd
from pathlib import Path

PASTA_SCRIPT = Path(__file__).resolve().parent
NOME_ARQUIVO = "funcionarios.csv"


candidatos = [
    PASTA_SCRIPT / NOME_ARQUIVO,
    PASTA_SCRIPT.parent / NOME_ARQUIVO,
    PASTA_SCRIPT.parent / "atividade1" / NOME_ARQUIVO,
    PASTA_SCRIPT.parent.parent / NOME_ARQUIVO,
]
base_de_dados = next((c for c in candidatos if c.exists()), None)


if base_de_dados is None:
    raiz = PASTA_SCRIPT
    while raiz.parent != raiz and not (raiz / ".venv").exists():
        raiz = raiz.parent
    if not (raiz / ".venv").exists():
        raiz = PASTA_SCRIPT.parents[3] if len(PASTA_SCRIPT.parents) > 3 else PASTA_SCRIPT.parent
    achados = sorted(raiz.rglob(NOME_ARQUIVO))
    if achados:
        base_de_dados = achados[0]
    else:
        raise FileNotFoundError(
            f"'{NOME_ARQUIVO}' não existe em nenhum lugar do projeto (raiz: {raiz}). "
            "Rode a atividade1 para gerá-lo ou crie o arquivo manualmente (veja abaixo)."
        )

print(f"Usando base de dados: {base_de_dados}")

arquivo_cargos_altos = PASTA_SCRIPT / "cargos_altos.csv"
colunas_base = ["id", "nome", "salario", "cargo"]

# 3) Ler o funcionarios.csv
df = pd.read_csv(base_de_dados, sep=";")
print("Colunas do funcionarios.csv:", df.columns.tolist())

faltando = [c for c in colunas_base if c not in df.columns]
if faltando:
    raise KeyError(f"Colunas faltando no arquivo original: {faltando}")

df = df[colunas_base].copy()
df["salario"] = pd.to_numeric(df["salario"], errors="coerce")
df["cargo"] = df["cargo"].astype(str).str.strip()

df_filtrado = df[df["salario"] > 6000].copy()
df_filtrado.to_csv(arquivo_cargos_altos, index=False, sep=";")

df_filtrado = pd.read_csv(arquivo_cargos_altos, sep=";")
print("\nFuncionários com salário acima de 6000:")
print(df_filtrado)

cargos_existentes = set(df["cargo"].str.lower())

novos_funcionarios = [
    {"id": 100, "nome": "João de Menezes", "salario": 150000, "cargo": "Instrutor"},
    {"id": 101, "nome": "Victor Sousa", "salario": 200000, "cargo": "Interpreter"},
]

for novo in novos_funcionarios:
    cargo_novo = str(novo["cargo"]).strip().lower()
    if cargo_novo in cargos_existentes:
        raise ValueError(f"O cargo '{novo['cargo']}' já existe. Use um cargo diferente.")
    cargos_existentes.add(cargo_novo)

df_filtrado = pd.concat([df_filtrado, pd.DataFrame(novos_funcionarios)], ignore_index=True)
print("\nApós cadastrar os novos funcionários:")
print(df_filtrado)

if len(df_filtrado) < 2:
    raise ValueError("Não há linhas suficientes para remover os índices 0 e 1.")

df_filtrado = df_filtrado.drop(index=[0, 1]).reset_index(drop=True)
print("\nApós remover os índices 0 e 1:")
print(df_filtrado)

tempos = [2, 6, 12, 9, 999]
if len(df_filtrado) != len(tempos):
    tempos = list(range(1, len(df_filtrado) + 1))

df_filtrado["tempo_empresa"] = tempos
df_filtrado["tempo_empresa"] = df_filtrado["tempo_empresa"].astype("int64")
print("\nApós criar a coluna tempo_empresa:")
print(df_filtrado)

estagiario = pd.DataFrame([
    {"id": 200, "nome": "Lucas", "salario": 1500, "cargo": "Estagiário", "tempo_empresa": 3}
])

df_filtrado = pd.concat([df_filtrado, estagiario], ignore_index=True)
df_filtrado["tempo_empresa"] = df_filtrado["tempo_empresa"].astype("int64")

df_filtrado = df_filtrado[colunas_base + ["tempo_empresa"]]
print("\nDataFrame final:")
print(df_filtrado)

df_filtrado.to_csv(arquivo_cargos_altos, index=False, sep=";")

df_conferencia = pd.read_csv(arquivo_cargos_altos, sep=";")

print("\nConteúdo final salvo em cargos_altos.csv:")
print(df_conferencia)
print("\nTipos das colunas:")
print(df_conferencia.dtypes)
print("\nValidações:")
print("Arquivo existe?", arquivo_cargos_altos.exists())
print("Total de linhas:", len(df_conferencia))
print("Colunas:", df_conferencia.columns.tolist())
print("tempo_empresa é inteiro?", pd.api.types.is_integer_dtype(df_conferencia["tempo_empresa"]))
print("Estagiário presente?", (df_conferencia["cargo"] == "Estagiário").any())
print("Salários acima de 6000:", int((df_conferencia["salario"] > 6000).sum()))