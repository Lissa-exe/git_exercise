import pandas as pd
def allmondays(year):
    return pd.date_range(start=str(year), end=str(year+1), freq='W-MON').strftime('%d/%m/%Y').tolist()

print(allmondays(2021))