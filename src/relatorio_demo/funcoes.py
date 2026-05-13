import pandas as pd

def resumo(df: pd.DataFrame, col: str) -> dict:
    return {
        'media': df[col].mean(),
        'mediana': df[col].median(),
        'desvio': df[col].std(),
    }
