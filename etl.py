import pandas as pd
import os
import glob

# Uma funcao de extract que le e consolida os json


def extrair_dados_e_consolidar(pasta: str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(pasta, '*.json'))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_total = pd.concat(df_list, ignore_index=True)
    print(df_total)
    return df_total

# uma funcao que transforma

def calcular_kpi_de_total_de_vendas(df: pd.DataFrame) -> pd.DataFrame:
    df['Total'] = df['Quantidade'] * df['Venda']
    return df

# uma funcao que da load em csv ou parquet
"""
parametro que vai ser ou "csv" ou "parquert" ou "os dois"
"""

def carregar_dados(df: pd.DataFrame, formatos: list):
    for formato in formatos:
        if formato == 'csv':
            df.to_csv("dados.csv", index=False)
        if formato == 'parquet':
            df.to_parquet("dados.parquet", index=False)


if __name__ == "__main__":
    pasta_argumento: str = 'data'
    data_frame = extrair_dados_e_consolidar(pasta=pasta_argumento)
    data_frame_calculado = calcular_kpi_de_total_de_vendas(data_frame)
    formato_de_saida: list = ["csv","parquet"]
    carregar_dados(data_frame_calculado, formato_de_saida)