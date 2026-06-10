import pandas as pd

def create_dataframe(data):
    """
    Returns: dict with 'data', 'shape', 'columns'
    """
    df = pd.DataFrame(data)
    op_dict = {
                'data': data,
                'shape': list(df.shape),
                'columns': list(df.columns) 
              }

    return op_dict