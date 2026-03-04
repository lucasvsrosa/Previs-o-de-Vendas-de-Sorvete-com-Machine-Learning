import pandas as pd

def carregar_dados(caminho_csv):
    return pd.read_csv(caminho_csv)

def salvar_dados(df, caminho_csv):
    df.to_csv(caminho_csv, index=False)
