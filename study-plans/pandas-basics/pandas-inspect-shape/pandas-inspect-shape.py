import pandas as pd

def inspect_dataframe(data):

    df = pd.DataFrame(data)
    op_df = {
        "rows": df.shape[0],
        "cols": df.shape[1],
        "columns": list(df.columns),
        "dtypes": {col: str(df[col].dtype) for col in df.columns},
        "total_values": int(df.shape[0]) * int(df.shape[1])
    }
    return op_df
    
    
    

    
    