import pandas as pd

df = pd.read_csv("dados_despadronizados.csv", dtype=str)

df["cpf_formatado"] = (
    df["cpf"]
    .fillna("")
    .str.replace(r"\D", "", regex=True)
)

df["cpf_valido"] = (
    df["cpf_formatado"]
    .str.fullmatch(r"\d{11}")
    .fillna(False)
    .astype(bool)
)


df["numero_formatado"] = (
    df["numero"]
    .fillna("")
    .str.replace(r"\D", "", regex=True)
)

df["numero_valido"] = (
    df["numero_formatado"]
    .str.fullmatch(r"\d{10,13}")
    .fillna(False)
    .astype(bool)
)


salario_limpo = (
    df["salario"]
    .astype(str)
    .str.strip()
    .str.replace(r"[^\d,.\-]", "", regex=True)
    .str.replace(r"\.(?=\d{3}(?:\D|$))", "", regex=True)
    .str.replace(",", ".", regex=False)
)

df["salario_formatado"] = pd.to_numeric(salario_limpo, errors="coerce")

df["salario_valido"] = df["salario_formatado"].notna()


colunas = [
    "nome",
    "cpf",
    "cpf_formatado",
    "cpf_valido",
    "numero",
    "numero_formatado",
    "numero_valido",
    "salario",
    "salario_formatado",
]

colunas_com_salario_valido = colunas + ["salario_valido"]


df[colunas_com_salario_valido].to_csv(
    "dados_padronizados.csv",
    index=False
)

print(df[colunas_com_salario_valido].head(20).to_string())