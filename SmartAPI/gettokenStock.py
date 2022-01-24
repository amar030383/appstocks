import pandas as pd
import requests

def angelOneStock():
    url = 'https://margincalculator.angelbroking.com/OpenAPI_File/files/OpenAPIScripMaster.json'
    d = requests.get(url).json()
    token_df = pd.DataFrame.from_dict(d)
    token_df['expiry'] = pd.to_datetime(token_df['expiry'])
    token_df = token_df.astype({'strike':float})
    df3= (token_df [['symbol','name', 'token', 'exch_seg']])
    from sqlalchemy import create_engine
    engine = create_engine('postgresql://username:password@localhost:5432/mydatabase')
    df3.to_sql('table_name', engine)
    return (df3)
   

df3 = angelOneStock()
save_posgresql(df3)