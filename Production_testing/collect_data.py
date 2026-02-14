import pandas as pd

class collected_data :

    def data_1d(df, a):
        return df.iloc[:, a].to_numpy()

    def data_2d(df, a):
        return print(df.iloc[:, a].to_numpy())