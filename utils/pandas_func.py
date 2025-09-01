import pandas as pd

def set_columns(columns, df: pd.DataFrame):
    
    df.columns = columns
    
    return df
