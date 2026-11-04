import pandas as pd
import numpy as np

df = pd.read_csv("estoque_supermercado.csv")

df["preco"] = (
    df["preco"]
    .astype(str)
    .str.replace(r"[^\d,.-]", "", regex=True)
    .str.replace(r",", ".", regex=False)
)
df["preco"] = pd.to_numeric(df["preco"], errors="coerce")

media_preco = df["preco"].mean()
df["preco"] = df["preco"].fillna(media_preco)

df["quantidade"] = pd.to_numeric(df["quantidade"], errors="coerce")

df["quantidade"] = df["quantidade"].fillna(0).astype(int)

df["setor"] = (
    df["setor"]
    .astype(str)
    .str.strip()
    .str.title()
)
df["setor"] = df["setor"].replace({"Nan": "Sem Setor", "": "Sem Setor"}).fillna("Sem Setor")

df["data_compra"] = pd.to_datetime(df["data_compra"], format="%d/%m/%Y", errors="coerce")
df["data_vencimento"] = pd.to_datetime(df["data_vencimento"], format="%d/%m/%Y", errors="coerce")

print("\n--- BASE DE DADOS LIMPA ---")
print(df[["nome", "preco", "quantidade", "setor", "data_compra", "data_vencimento"]].head())


data_atual = pd.to_datetime("27/10/2026", format="%d/%m/%Y")
inicio_semana = data_atual
fim_semana = pd.to_datetime("03/11/2026", format="%d/%m/%Y")

mask_vencimento = (df["data_vencimento"] >= inicio_semana) & (df["data_vencimento"] <= fim_semana)
df_vencendo_semana = df[mask_vencimento].copy()

print("\n--- PRODUTOS VENCENDO ESTA SEMANA ---")
print(df_vencendo_semana[["nome", "data_vencimento", "quantidade"]].to_string(index=False))

print("\n--- MAIOR QUANTIDADE A VENCER ---")
if not df_vencendo_semana.empty:
    idx_maior_qtd = df_vencendo_semana["quantidade"].idxmax()
    produto_destaque = df_vencendo_semana.loc[idx_maior_qtd]
    data_fmt = produto_destaque["data_vencimento"].strftime("%d/%m/%Y")
    print(f"Produto: {produto_destaque['nome']} | Quantidade: {produto_destaque['quantidade']} | Vencimento: {data_fmt}")
else:
    print("Nenhum produto com vencimento nesta semana.")

inicio_compra = pd.to_datetime("24/10/2026", format="%d/%m/%Y")
fim_compra = pd.to_datetime("27/10/2026", format="%d/%m/%Y")
mask_compra = (df["data_compra"] >= inicio_compra) & (df["data_compra"] <= fim_compra)
df_compras_recentes = df[mask_compra]

print("\n--- COMPRAS RECENTES (24/10/2026 a 27/10/2026) ---")
print(df_compras_recentes[["nome", "data_compra"]].to_string(index=False))

df_sem_vencimento = df[df["data_vencimento"].isna()]

print("\n--- PRODUTOS SEM VENCIMENTO (NaT) PARA CONFERÊNCIA ---")
print(df_sem_vencimento[["nome", "data_vencimento"]].to_string(index=False))

df["valor_total_estoque"] = df["quantidade"] * df["preco"]
valor_por_setor = df.groupby("setor")["valor_total_estoque"].sum().sort_values(ascending=False)

print("\n--- MAIOR VALOR PATRIMONIAL POR SETOR ---")
print(valor_por_setor.apply(lambda x: f"R$ {x:,.2f}").to_string())
print(f"\n🏆 Setor com MAIOR valor financeiro total parado no estoque: {valor_por_setor.idxmax().upper()} (R$ {valor_por_setor.max():,.2f})")